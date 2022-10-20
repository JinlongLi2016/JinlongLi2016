# _*_ coding: utf-8 _*_
"""
Author:   Jinlong.Li
File:     vectornet.py
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from easydict import EasyDict

# cfg 定义了输入给网络的特征维度相关的信息
# obj_fea: Agent features of shape (B, A, N, D1). `Note: A[0] is ego`
# static_fea: Static features of shape(B, M, N, D2)
# vocsize: obj_fea & static_fea特征最后维度为类型信息(int),因此采用word_embedding层编码.
cfg = EasyDict(
    dict(
        vocsize=30,  # num_embedding
        A=200,
        M=100,
        N=16,
        D1=10,
        D2=10,
        ego_index=0,
        max_num_lanes=
        5,  # the first `max_num_lanes` feature in `static_fea` is lane
        max_num_agents=50,
        tp=50,
        tf=50,  # num time steps of future
    ))


class MessagePassing(nn.Module):
  """Broadcast neighbors' info to center node"""

  def __init__(self, fea_dim):
    super().__init__()
    self.fc = nn.Sequential(nn.Linear(fea_dim, fea_dim // 2), nn.ReLU(),
                            nn.LayerNorm(fea_dim // 2))
    self.maxpool1d = nn.MaxPool1d(N)

  def forward(self, fea):
    fea = self.fc(fea)
    B, N, D = fea.shape
    fea = fea.permute((0, 2, 1))

    fea_maxpooled = F.max_pool1d(fea, kernel_size=N)
    ret = torch.cat([fea, fea_maxpooled.repeat((1, 1, N))], dim=1)
    ret = ret.permute((0, 2, 1))
    return ret


class SubGraph(nn.Module):
  """encode each polyline in subgraph"""

  # input (B, N, D) -> (B, D2) # 将时序维度reduce,形成一个feature vector.
  # `A` subgraph vs `M` subgraph 区别在与维度上面
  def __init__(self, graph_node_dim, num_nodes, feature_dim, vocabular_size,
               wordembedding_size):
    """
      graph_node_dim: 最后一个维度为type(int)信息,使用word embedding编码为wordembedding_size维度.
                      前面的维度为 vector start end point loc,  对于object则还有speed info(vx, vy, ax, ay).
                      维度转换为 (feature_dim - wordembedding_size) 
      feature_dim:  map graph node to feature_dim size.
      vocabular_size: word embedding layers vocabulary size
      wordembedding_size: represet word(a int number) as a wordembedding_size dimential vector
    """
    super().__init__()
    # @TODO:do some assertion on dimention compatibility
    residual_feature_dim = feature_dim - wordembedding_size
    # [B, N, D-1] -> [B, N, residual_feature_dim]
    self.residual_feature_fc = nn.Sequential(
        nn.Linear(graph_node_dim - 1, residual_feature_dim), nn.ReLU(),
        nn.LayerNorm(residual_feature_dim))
    # we layer  [B, N,] -> [B, N, wordembedding_size]
    self.word_embedding = nn.Embedding(vocabular_size, wordembedding_size)

    # [B, N, feature_dim] -> [B, N, feataure_dim]
    self.message_passing_layers = []
    for _ in range(3):
      self.message_passing_layers.append(MessagePassing(feature_dim))

  def forward(self, feature):
    """
        params:
            feature : (B, 16, -1)
        return:  
            feature B, feature_dim
    """
    res_feature = self.residual_feature_fc(feature[..., :-1])
    word_embedding = self.word_embedding(feature[..., -1].long())
    fea = torch.cat([res_feature, word_embedding], dim=-1)
    for graph_layer in self.message_passing_layers:
      fea = graph_layer(fea)
    fea = fea.permute((0, 2, 1))

    fea = F.max_pool1d(fea, fea.size(-1))  # [B, feature_dim]
    return fea


class VectorGraph(nn.Module):

  def __init__(self, fea_dim):
    super().__init__()
    self.query_fc = nn.Linear(fea_dim, fea_dim // 2)
    self.key_fc = nn.Linear(fea_dim, fea_dim // 2)
    self.value_fc = nn.Linear(fea_dim, fea_dim)

  def forward(self, graph_features):
    """
    Param:
      graph_features: [B, P, D] # P = A + M
    Return:
      so
    """
    query = self.query_fc(graph_features)
    key = self.key_fc(graph_features)
    values = self.value_fc(graph_features)
    attention = torch.bmm(query, key.transpose(-1, -2))
    weights = F.softmax(attention, dim=2)
    y = torch.bmm(weights, values)
    return y


class VectorNetEncoder(nn.Module):
  """Encode Agent and Map info using subgraph & global graph"""

  def __init__(self, cfg, fea_dim, embedding_dim):
    """
    obj_fea: Agent features of shape (B, A, N, D1). `Note: A[0] is ego`
    static_fea: Static features of shape(B, M, N, D2)
    Param:
      cfg: 
      fea_dim: in what feature dim we transform node features
      embedding_dim: WordEmbedding Type(a int) 
    """
    super().__init__()
    A, M, N, D1, D2 = cfg.A, cfg.M, cfg.N, cfg.D1, cfg.D2
    self.obj_subg = SubGraph(D1, N, fea_dim, cfg.vocsize, embedding_dim)
    self.static_subg = SubGraph(D2, N, fea_dim, cfg.vocsize, embedding_dim)

    self.vector_graph = VectorGraph(fea_dim=fea_dim)

  def forward(self, obj_fea, static_fea):
    """
    param:
      obj_fea: Agent features of shape (B, A, N, D1). `Note: A[0] is ego`
      static_fea: Static features of shape(B, M, N, D2)
    return:
      polyline_features: (B, P, D) # P = A + M, D = feature_dim
    """
    B, A, N, D1 = obj_fea.shape
    obj_graph_feas = self.obj_subg(obj_fea.view(-1, N, D1))
    obj_graph_feas = obj_graph_feas.view(B, A, -1)

    # t = []
    # for i in range(B):
    #   t.append(self.obj_subg(obj_fea[i]))
    # tstack = torch.stack(t)
    # tstack = torch.squeeze(tstack)
    # print("so a check", (obj_graph_feas - tstack).max())
    # # so a check tensor(0., grad_fn=<MaxBackward1>)

    B, M, N, D2 = static_fea.shape
    static_graph_feas = self.static_subg(static_fea.view(-1, N, D2))
    static_graph_feas = static_graph_feas.view(B, M, -1)

    # print(obj_graph_feas.shape)
    # print(static_graph_feas.shape)
    polylines_features = torch.cat((obj_graph_feas, static_graph_feas), dim=-2)

    polylines_features = self.vector_graph(polylines_features)
    return polylines_features


class GeneralizedLinearSeq(nn.Module):

  def __init__(self, feature_dims, last_layer_with_activation=False):
    super().__init__()
    assert len(feature_dims) > 2
    num_layers = len(feature_dims) - 1
    layers = []
    for l in range(num_layers):
      if l != num_layers - 1 or last_layer_with_activation:  # last layer
        layers.extend([
            nn.Linear(feature_dims[l], feature_dims[l + 1]),
            nn.ReLU(),
            nn.LayerNorm(feature_dims[l + 1]),
        ])
      else:
        layers.extend([nn.Linear(feature_dims[l], feature_dims[l + 1])])
    self.seq = nn.Sequential(*layers)

  def forward(self, features):
    return self.seq(features)


class Decoder(nn.Module):
  """Decode ego planning(which path and its traj) & others prediction"""

  def __init__(self, cfg, feature_dim: int):
    """
    Params:
      cfg: cfg of network settings
      feature_dim: polyline's subgraph features
    Return:

    """
    super().__init__()
    self.cfg = cfg

    self.cls_head = GeneralizedLinearSeq([feature_dim, 64, 32, 1])
    self.planning_head = GeneralizedLinearSeq(
        [feature_dim, feature_dim, cfg.tf * 2])
    self.prediciton_head = GeneralizedLinearSeq(
        [feature_dim, feature_dim, cfg.tf * 2])

  def forward(self, features):
    """
    Params:
      features: of shape(B, P: A+M, D), representing ego&agents' features
    Return:
    """
    cfg = self.cfg
    # cls & planning
    ego_feature_indices = [cfg.ego_index]
    lane_feature_indices = list(range(cfg.A, cfg.A + cfg.max_num_lanes))
    ego_and_lane_feature = features[:, ego_feature_indices,...] + \
      features[:, lane_feature_indices, ... ] # broadcast to get[B, max_num_lanes, D]
    logits = self.cls_head(ego_and_lane_feature)  # [B, max_num_lanes, 1]
    logits = torch.squeeze(logits)
    scores = F.softmax(logits, dim=-1)
    plan_trajs = self.planning_head(ego_and_lane_feature)
    # prediction # 100 agents除了ego,其他的动态障碍物有？维护了一个semantic_enum,表明哪些维度是DynamicAgent的维度
    agents_feature_indces = list(range(1, 1 + cfg.max_num_agents))
    agents_feature = features[:, agents_feature_indces]
    pred_trajs = self.prediciton_head(
        agents_feature)  # [B, cfg.max_num_agents, cfg.tf * 2]

    print(f"scores: shape {scores.shape}, {plan_trajs.shape}, {pred_trajs.shape}")
    return logits, plan_trajs, pred_trajs


if __name__ == "__main__":
  B, N, D = 64, 16, 9

  # X = torch.rand(B, N, D)
  # X[..., -1] = 5

  # sg = SubGraph(D, N, 96, 10, 32)
  # ret = sg(X)
  # print(ret.shape)
  ve = VectorNetEncoder(cfg, fea_dim=96, embedding_dim=32)

  print("static raw feature shape: ", B, cfg.M, N, cfg.D2)
  static_feas = torch.rand(B, cfg.M, N, cfg.D2)
  static_feas[..., -1] = 8
  print("agent raw feature shape: ", B, cfg.A, N, cfg.D1)
  X = torch.rand(B, cfg.A, N, cfg.D1)
  X[..., -1] = 5
  polyline_features = ve(X, static_feas)
  print(f"{polyline_features.shape}")

  mask = [1, 3]
  print(
      f"{X.shape}, {X[:, mask, ...].shape, {X[1:1+1].shape}} {(X[[1]] + X).shape}"
  )
  print(f"{X.mean()}, {X[1:1+1].mean()}, {(X[1:1+1] + X).mean()}")

  dec = Decoder(cfg, feature_dim=96)
  dec(polyline_features)
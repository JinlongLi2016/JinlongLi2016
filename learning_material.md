> note: 某些链接是非空开的

### PNC算法学习

- Data-Driven/End2End
  - [Notion](https://www.notion.so/captaincaptain/PNC-Task-672f7614bb274fff9dc0aeadba50ad64?pvs=4): 数据驱动PNC && [DayStore](https://gitlab.com/JinlongLi2016/daystore/-/tree/master/202205/0528/DDP): Data-Driven Planning
  - [Algorithm｜dd | VectorNet](https://www.notion.so/captaincaptain/VectorNet-c3e44de346184e6e85b29f26c8ca9392?pvs=4) [code](./codes/vectornet.py)
  - Algorithm｜e2e | Can Autonomous Vehicles Identify, Recover From, and Adapt to Distribution Shifts?, 2000
  - Algorithm｜e2e | Causal Confusion in Imitation Learning, 1900
  - Algorithm｜e2e | DTPP: Differentiable Joint Conditional Prediction and Cost Evaluation for Tree Policy Planning in Autonomous Driving, 2300
  - Algorithm｜e2e | **VADv2**: End-to-End Vectorized Autonomous Driving via Probabilistic Planning, 2402
  - Algorithm｜e2e | DriveVLM: The Convergence of Autonomous Driving and Large Vision-Language Models
  - Algorithm｜e2e | PiP: Planning-informed Trajectory Prediction for Autonomous Driving, 2000
  - Algorithm｜e2e | Scene Transformer: A unified architecture for predicting multiple agent trajectories,2103
    * 模型输入为perception object
    * 使用mask来支持同步做planning&prediction
  - Algorithm｜e2e | LOKI: Long Term and Key Intentions for Trajectory Prediction
  - Algorithm｜e2e | MP3: A unified model to map, perceive, predict and plan
  - Algorithm｜e2e | TNT
  - Algorithm｜e2e | DenseTNT
  - Algorithm｜e2e | MultiPath
  - Algorithm｜e2e | MultiPath++
    
    贡献有三点
    
    1. 精心设计下面几个方面提高效果：输入的表征及编码，融合编码及输出的分布。considering choices for input representation and encoding, fusing encodings, and representing the output distribution.
    2. 证明了以下几个方面对于行为预测很重要：稀疏编码，高效融合方法，基于控制的方法以及可学习的锚 （sparse encoding, efficient fusion methods, control-based methods, and learned anchors）
    3. we provided a practical guide for various tricks used for training and inference to improve **robustness, increase diversity, handle missing data, and ensure fast convergence** during training.
  
- Algorithm｜e2e | **Hydra-MDP**: End-to-end Multimodal Planning with Multi-target Hydra-Distillation, 2406
- Algorithm｜e2e | GenAD: Generative End-to-End Autonomous Driving
- Algorithm｜e2e | MotionLLM
- Algorithm｜e2e | GUMP
- [Algorithm｜MPDM]()
- [Algorithm｜EUDM]()
- [Algorithm｜Spatial-temporal Semantic Corridor(SSC)]()
- [Algorithm｜EPSILON]()
- [Algorithm｜MDP](https://www.notion.so/captaincaptain/MDP-205cfd0f3c3a47aa8f4892025be18280?pvs=4) && [Algorithm｜POMDP]()
- [Algorithm｜Planning on a (Risk) Budget: Safe Non-Conservative Planning in Probabilistic Dynamic Environments]()
- Algorithm | Synthesis and Stabilization of Complex Behaviors through Online Trajectory Optimization(iLQR/DDP)
- [Algorithm｜MultiPath]() && [Algorithm｜MultiPath++](https://www.notion.so/captaincaptain/MultiPath-3a65a20faed34a27a75811cdcc72ffaa?pvs=4)
- Algorithm｜[IDM Driver](https://www.notion.so/captaincaptain/IDM-aca9dbf1d2dd48bd9ab8b6b9b5af6701?pvs=4) & [MOBIL](https://www.notion.so/captaincaptain/MOBIL-15ddc85a1b46497a9f449a2abfea24fc?pvs=4) Model
- [Algorithm｜MARC: Multipolicy and Risk-aware Contingency Planning for Autonomous Driving, 2308](https://arxiv.org/abs/2308.12021)  
- Algorithm | [Contingency Plan] Contingency Model Predictive Control for Automated Vehicles, 1907  
- Algorithm | [Contingency Plan] Contingency Model Predictive Control for Linear Time-Varying Systems, 2102  
- Algorithm | 使用branch MPC进行交互多模态运动规划 Interactive multi-modal motion planning with Branch Model Predictive Control, 2110
- Algorithm | 抵达集/可达集(Reach Set & Reachable Set) Bridging the Gap Between Safety and Real-Time Performance in Receding-Horizon Trajectory Design for Mobile Robots, 1809
- [Algorithm｜Spatio-temporal Motion Planning for Autonomous Vehicles with Trapezoidal Prism Corridors and Be ́zier Curves(todo)]()


### 基础算法学习

* [Algorithm｜图网络(GNN)](https://www.notion.so/captaincaptain/GNN-1e7c51101fb64aebbc890b59b307e8ac?pvs=4)
* [Algorithm｜强化学习](https://www.notion.so/captaincaptain/1bc85dee768c4024af9cfce12cd605d1?pvs=4)
* [Algorithm｜状态栅格 state lattice planner](https://www.notion.so/captaincaptain/1bc85dee768c4024af9cfce12cd605d1?pvs=4)
* [Algorithm｜PWJ: Piecewise Jerk Optimizer(path & speed)](https://www.notion.so/captaincaptain/PWJ-Piecewise-Jerk-Optimizer-path-speed-ded75d987c864f5f97e85c262cc05c12?pvs=4)
* [Algorithm｜规划｜常用算法](https://www.notion.so/captaincaptain/64fb1d75f0e74edda50d151d921a433a?pvs=4)
  * [A*]()
  * [RRT&RRT*]()
  * [人工势场法(Artificial Potential Field)]()
  * [Optimal Trajectory In Frenet Frame](https://captaincaptain.notion.site/ecacdf9a2c4246cdb82ada3f1a48f5a5)
* Curve
  * [Bezier Curve 贝塞尔曲线]()  
    1. 端点插值
    1. 凸包性：贝塞尔曲线
    1. hodograph性质: 它的导数依旧是贝塞尔曲线
    1. 固定时间间隔：每一段定义在[0, 1]间
  * [Clothoid/Spiral（螺线）](https://github.com/JinlongLi2016/DayStore/blob/master/202205/0528/PlanningInANutshell.md#%E6%80%BB%E7%BB%93)
  * Quintic Polynomial
* Spline 样条曲线
  * [Cubic Spline](https://github.com/JinlongLi2016/DayStore/tree/master/202110/1022/spline)
  * [Quintic Spline]()
  * [BSpline (Basis-Spline)](https://github.com/JinlongLi2016/DayStore/blob/master/202205/0528/PlanningInANutshell.md#b%E6%A0%B7%E6%9D%A1basis-spline)
  * [G2-Quintic Spline](https://www.notion.so/captaincaptain/G2-Quintic-Spline-22ca407457f24d0bafffa3304b4b8561?pvs=4), [code](https://github.com/JinlongLi2016/DayStore/tree/master/topics/g2-quintic-spline)

* Control 
  * [LQR](https://www.youtube.com/watch?v=E_RDCFOlJx4) | 线性二次调节器: 状态转移关系是线性的，目标函数是二次的调节器.   
    1. 设计线性的转移方程
    2. 调节矩阵 Q, R的值使得效果最优. Q 对角阵每个值是其对应状态维度的error惩罚weight. R 是 控制维度 weight
    3. 寻找最优的gain set: k = lqr(Q, B, Q, R)

  * MPC | 模型预测控制
    1. 估计/测量系统当前状态
    2. 基于转移方程和目标函数优化 控制序列 u(k), u(k+1), ..., u(k+N-1)
    3. 取最开始的u(k)控制输入到控制器 (滚动优化)  

    MPC每一轮滚动优化可以使用LQR
    
  * [iLQR(DeepNote - iLQG)/DDP](https://deepnote.com/workspace/cap-219c-adf529b6-5576-4633-8243-086b31bd81c6/project/103-Iterative-Linear-Quadratic-Regulator-CourseNodes-ddfe3b21-6b96-4d14-b5d2-f122e0af1143/notebook/ilqr_driving-73702070a18b4db3ad7b82ae3c5e1281) [Gitee-ddp](https://gitee.com/jlliwhale/ddp)

### 在线学习课程

- [课程｜多伦多大学-无人驾驶课程](https://captaincaptain.notion.site/ecacdf9a2c4246cdb82ada3f1a48f5a5)
- [课程｜深蓝学院-运动规划课程](https://gitlab.com/JinlongLi2016/captain-motionplan/-/tree/master)
- [课程｜深蓝学院-决策预测课程]()

### 编程

* C++/Python/Matlab
* Tensorflow/PyTorch

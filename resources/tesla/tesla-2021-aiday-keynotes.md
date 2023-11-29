# cap-keynotes

keywords:

- [ ] HydraNets
- [ ] Transformer
- [ ] RegNet 
- [ ] BiFPN
- [ ] EfficientDet

  - sensory systems

    | 神经网络不可避免的三个问题                | 三个问题对应的解决方案                                       |
    | ----------------------------------------- | ------------------------------------------------------------ |
    | 单backbone vs 多种不同任务                | **HydraNets**                                                |
    | 图像空间预测  vs 不足以在三维空间进行导航 | **From image to vector space**                               |
    | 基于帧进行处理 vs 无记忆                  | **Memory storage** to provide past info — either space-wise or temporal-wise( **“feature queue” to imbue the NN with a sort of memory store**.) |

    Processing **videos instead of frames**, together with **vector space predictions**, provide prediction robustness to the system. **Multicamera and multi-frame processing both provide great amounts of robustness and precision to the overall system.**

    * 基于HydraNets,多种任务共享backbone，网络可以检测车辆、行人，重建道路的面、线，和识别交通信号及交通灯。
    * 图像、向量空间的转换自有视觉系统以来就有了。目前关键的不同之处是在predictions之前进行转换。
      * 从图像空间到向量空间，transformer是最好的选择。图像空间的每个像素都会和3D向量空间的一个特定位置相关连。
      * 在向量空间进行预测还有一个好处是更鲁棒，每一个相机的信息都会为vector space提供信息。
      * 图像空间与3D向量空间预测结果对比![prediction-in-image-vs-vectorspace](./resources/prediction-in-image-vs-vectorspace.jpg)
    *  **“feature queue” to imbue the NN with a sort of memory store**. 特征队列输入为每一帧，通过 空间递归神经网络来生成视频

  - motor systems

    空间非凸+高维  

    离散搜索算法解决可以非凸，但是计算代价较高。另一方面，连续函数优化算法在高维空间很容易落于局部最优。

    * Explicit planning

      Tesla采取了混合的方式:　基于视觉系统给出的向量空间，**粗搜**出一个凸的走廊，然后使用**连续优化方法**来获得平滑得轨迹。

      To recap, here are the main points about the planning and control system:

      * <u>Safety, comfort, and efficiency</u> are maximized. | 最大化 安全、舒适、效率性
      * A hybrid approach combining coarse search and continuous optimization functions solves <u>both non-convexity and high-dimensionality.</u> | 使用混合的方式来解决**非凸和高维**的问题：粗搜再使用连续优化。
      * The system first searches for the best set of trajectories, <u>the convex corridor, using physical models.</u> | 首先使用physical models来搜凸的走廊
      * Then it finds a definitive solution using continuous optimization methods. | 再使用连续优化方法来寻找一个确定的答案
      * The control system carries out the planned solution to get the car to the destination.

    * Learning-based planning

      * **A combination of <u>neural networks and Monte-Carlo Tree Search (MCTS)</u>** **provides a global solution**

  - [Here’s](https://youtu.be/j0z4FweCy4M?t=5021) the complete architecture of the visual, planning, and control systems:

    1. The vision NN transforms image data into vector space predictions.
    2. Those predictions — together with intermediate-level features — go into the NN planner — still under development — which is mainly used to generate trajectory distributions in complex situations, such as driving in a city center.
    3. The visual NN can be trained end-to-end together with the NN planner, using explicit cost functions like safety, comfort, or efficiency measures.
    4. Vector space predictions and the trajectory distribution are then fed into the explicit planner so it can generate the actual steering and acceleration commands.
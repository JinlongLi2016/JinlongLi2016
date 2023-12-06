> note: 某些链接是非空开的

### PNC算法学习

- [Algorithm｜MPDM]()
- [Algorithm｜EUDM]()
- [Algorithm｜Spatial-temporal Semantic Corridor(SSC)]()
- [Algorithm｜EPSILON]()
- [Algorithm｜MDP](https://www.notion.so/captaincaptain/MDP-205cfd0f3c3a47aa8f4892025be18280?pvs=4) && [Algorithm｜POMDP]()
- [Algorithm｜Planning on a (Risk) Budget: Safe Non-Conservative Planning in Probabilistic Dynamic Environments]()
- Algorithm | Synthesis and Stabilization of Complex Behaviors through Online Trajectory Optimization(iLQR/DDP)
- [Algorithm｜VectorNet](https://www.notion.so/captaincaptain/VectorNet-c3e44de346184e6e85b29f26c8ca9392?pvs=4)
- [Algorithm｜MultiPath]() && [Algorithm｜MultiPath++](https://www.notion.so/captaincaptain/MultiPath-3a65a20faed34a27a75811cdcc72ffaa?pvs=4)
- Algorithm｜[IDM Driver](https://www.notion.so/captaincaptain/IDM-aca9dbf1d2dd48bd9ab8b6b9b5af6701?pvs=4) & [MOBIL](https://www.notion.so/captaincaptain/MOBIL-15ddc85a1b46497a9f449a2abfea24fc?pvs=4) Model
- [Algorithm｜MARC: Multipolicy and Risk-aware Contingency Planning for Autonomous Driving(todo)](https://arxiv.org/abs/2308.12021)
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
  * [Bezier Curve]()
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
    
  * [iLQR(iLQG)/DDP](https://deepnote.com/workspace/cap-219c-adf529b6-5576-4633-8243-086b31bd81c6/project/103-Iterative-Linear-Quadratic-Regulator-CourseNodes-ddfe3b21-6b96-4d14-b5d2-f122e0af1143/notebook/ilqr_driving-73702070a18b4db3ad7b82ae3c5e1281)

### 在线学习课程

- [课程｜多伦多大学-无人驾驶课程](https://captaincaptain.notion.site/ecacdf9a2c4246cdb82ada3f1a48f5a5)

### 编程

* C++/Python/Matlab
* Tensorflow/PyTorch
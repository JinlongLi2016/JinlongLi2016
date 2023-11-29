# V12: 端到端模型实现辅助驾驶

> “And there's a bicyclist. Again, there is no line of code that says give clearance to bicyclists. It is just doing what people do. It can read signs without ever being taught to read. Once again, there is no line of code that says stop at a stop sign or wait for another car. There's no ‘wait x number of seconds,’ nothing like that. This is all nets, baby, nothing but net.”

*  端到端模型：输入相机数据,输出
* 消除了对行为直接编程，均从数据中去模仿人的行为
    30万行代码 -> 3千行
    * 适应性更好
    * 可以不断地学习
* 需要高质量数据
    数据采集

# take out
1. 看起来采用的是通过视频进行模仿学习.  
    [input] 相机图像-> [output] 控制(方向盘、油门刹车)（elon提到：没有告诉模型这是一个交通标志,是模型自己从图像中去学)

1. 对数据质量/分布把握是关键
    迭代自动程度相当高,基本上完全消除人工参与

1. 可以以50fps运行,受限于相机36fps

# 参考
1. [UNCUT: Elon Musk’s MIND BLOWING Live Tesla FSD Demo](https://www.youtube.com/watch?v=aqsiWCLJ1ms&ab_channel=SolvingTheMoneyProblem)
1. [FSD V12 Takeaways - A New Era (Elon’s Sneak Peek)](https://www.youtube.com/watch?v=ZI7-Swmuo4A&ab_channel=AIDRIVR)
1. [[BREAKING] Tesla Car Drives Elon Musk in Epic Livestream (FSD V12): NOTHING BUT NETS–All The Way Down!](https://blog.finxter.com/breaking-tesla-car-drives-elon-musk-in-epic-livestream-fsd-v12-nothing-but-nets-all-the-way-down/)
1. [FSD V12 (end to end AI)](https://teslamotorsclub.com/tmc/threads/fsd-v12-end-to-end-ai.301471/page-9)
1. [Breakdown: How Tesla will transition from Modular to End-To-End Deep Learning](https://www.thinkautonomous.ai/blog/tesla-end-to-end-deep-learning/)

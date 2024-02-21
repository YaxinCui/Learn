import numpy as np
# 代码来源：https://www.bilibili.com/video/BV13a4y1J7bw

# 对于一个agent，如何存储状态
class SmartAgent():

    def __init__(self, OOXX_index, Epsilon=0.05, LearningRate=0.2) -> None:
        self.value = np.zeros((3,3,3,3,3,3,3,3,3))
        # 9个格子，每个格子的状态，没有棋子，A下，B下
        # 每个状态的价值函数
        self.currentState = np.zeros(9)
        # 现在的状态
        self.previousState = np.zeros(9)
        # 上一步状态
        self.index = OOXX_index
        self.epsilon = Epsilon
        self.alpha = LearningRate

    def reset(self):
        self.currentState = np.zeros(9)
        self.previousState = np.zeros(9)
        # 0 代表没有棋子

    def actionTake(self, State):
        state = State.copy()
        available = np.where(state==0)[0]
        # 可填的空
        length = len(available)
        if length == 0:
            # 没有位置可以下了
            return state
        else:
            random = np.random.uniform(0,1)
            if random < self.epsilon:
                choose = np.random.randint(length)
                state[available[choose]] = self.index
                # 随机下这个位置
            else:
                tempValue = np.zeros(length)
                # 计算每个可行动作的价值
                for i in range(length):
                    tempState = state.copy()
                    tempState[available[i]] = self.index
                    tempValue[i] = self.value[tuple(tempState.astype(int))]
                    # 查询价格函数，tempState.astype(int)到底是干什么的？
                choose = np.where(tempValue==np.max(tempValue))[0]
                chooseIndex = np.random.randint(len(choose)) # 从最好的里面，随机选一个最好的
                state[available[choose[chooseIndex]]] = self.index
            # 更新状态
            return state

    def valueUpdate(self, State):
        self.currentState = State.copy()
        self.value[tuple(self.previousState.astype(int))] += \
            self.alpha*(self.value[tuple(self.currentState.astype(int))] - self.value[tuple(self.previousState.astype(int))])
        # 来源视频第3分钟，不需要游戏结束，就能更新价值函数
        # 蒙特卡诺、时序差分法的雏形
        self.previousState = self.currentState.copy()
# 1.循环队列
M = 100  # 全局变量，假设容量为100

class CSqQueue:  # 循环队列类
    def __init__(self):  # 构造方法
        self.data = [None] * M  # 存放队列中元素
        self.front = 0  # 队头指针
        self.rear = 0  # 队尾指针

    # 队列的基本运算算法
    # 1.判断队列是否为空
    def empty(self):
        return self.front == self.rear

    # 2.判断队列是否已满
    def full(self):
        return (self.rear + 1) % M == self.front

    # 3.x入队
    def push(self, x):
        assert not self.full()  # 队列未满
        self.rear = (self.rear + 1) % M
        self.data[self.rear] = x

    # 4.出队
    def pop(self):
        assert not self.empty()  # 队列不为空
        self.front = (self.front + 1) % M
        return self.data[self.front]

    # 5.取队首
    def getFront(self):
        assert not self.empty()  # 队列不为空
        return self.data[(self.front + 1) % M]

    # 6.求队列的大小
    def getSize(self):
        return (self.rear - self.front + M) % M

# 测试程序
q = CSqQueue()
for i in range(1, 6):
    q.push(i)

while not q.empty():
    print(q.pop())
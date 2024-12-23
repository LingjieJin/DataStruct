# 循环队列
class CSqQueue:
    def __init__(self, capacity):
        self.data = [None] * capacity  # 存放队列中元素
        self.front = 0  # 队头指针
        self.rear = 0  # 队尾指针
        self.capacity = capacity

    # 判断队列是否为空
    def empty(self):
        return self.front == self.rear

    # 判断队列是否已满
    def full(self):
        return (self.rear + 1) % self.capacity == self.front

    # 入队
    def push(self, x):
        assert not self.full()  # 队列未满
        self.rear = (self.rear + 1) % self.capacity
        self.data[self.rear] = x

    # 出队
    def pop(self):
        assert not self.empty()  # 队列不为空
        self.front = (self.front + 1) % self.capacity
        return self.data[self.front]

    # 取队首
    def getFront(self):
        assert not self.empty()  # 队列不为空
        return self.data[(self.front + 1) % self.capacity]

    # 求队列的大小
    def getSize(self):
        return (self.rear - self.front + self.capacity) % self.capacity

# 约瑟夫环问题
def josephus(n, k, m):
    q = CSqQueue(n + 1)  # 创建容量为 n+1 的循环队列
    for i in range(1, n + 1):
        q.push(i)  # 将所有人入队

    # 将队列前 k-1 个人移到队尾
    for _ in range(k - 1):
        q.push(q.pop())

    result = []
    while not q.empty():
        # 数到第 m 个人出列
        for _ in range(m - 1):
            q.push(q.pop())
        result.append(q.pop())

    return result

# 测试程序
n, k, m = 5, 1, 3
result = josephus(n, k, m)
print(",".join(map(str, result)))  # 输出: 3,1,5,2,4
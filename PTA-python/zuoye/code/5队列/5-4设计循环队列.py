class MyCircularQueue:

    def __init__(self, k: int):
        # 初始化队列，设置容量为 k
        self.queue = [0] * k
        self.head = 0
        self.tail = 0
        self.size = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        # 如果队列已满，返回 False
        if self.isFull():
            return False
        # 将元素添加到队尾
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True

    def deQueue(self) -> bool:
        # 如果队列为空，返回 False
        if self.isEmpty():
            return False
        # 移除队首元素
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        # 如果队列为空，返回 -1
        if self.isEmpty():
            return -1
        # 返回队首元素
        return self.queue[self.head]

    def Rear(self) -> int:
        # 如果队列为空，返回 -1
        if self.isEmpty():
            return -1
        # 返回队尾元素
        return self.queue[(self.tail - 1 + self.capacity) % self.capacity]

    def isEmpty(self) -> bool:
        # 判断队列是否为空
        return self.size == 0

    def isFull(self) -> bool:
        # 判断队列是否已满
        return self.size == self.capacity
    
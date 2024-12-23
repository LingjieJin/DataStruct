# 2.链队
class LinkNode:  # 链队结点类
    def __init__(self, x=None):  # 构造方法
        self.data = x  # 数据域
        self.next = None  # 指针域

class LinkQueue:  # 链队类
    def __init__(self):  # 构造方法
        self.front = LinkNode()  # 队首，创建带头结点
        self.rear = self.front  # 队尾指针

    # 队列的基本运算算法
    # 1.判断队列是否为空
    def empty(self):
        return self.front.next is None

    # 2.x入队
    def push(self, x):
        new_node = LinkNode(x)
        self.rear.next = new_node
        self.rear = new_node

    # 4.出队
    def pop(self):
        assert not self.empty()
        p = self.front.next
        self.front.next = p.next  # 删除队首
        if self.front.next is None:  # 如果队列为空，更新队尾指针
            self.rear = self.front
        return p.data

    # 5.取队首
    def getFront(self):
        assert not self.empty()
        return self.front.next.data

    # 6.求队列的大小
    def getSize(self):
        size = 0
        p = self.front.next
        while p is not None:
            size += 1
            p = p.next
        return size

# 测试程序
q = LinkQueue()
for i in range(1, 6):
    q.push(i)
print(q.getSize())
while not q.empty():
    print(q.pop())

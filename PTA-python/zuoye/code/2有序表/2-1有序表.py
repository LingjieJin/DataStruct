class SqList:
    # 0.构造方法
    def __init__(self):
        self.initcapcity = 10            # 初始容量
        self.capcity = self.initcapcity  # 最大存储
        self.data = [None] * self.capcity # 顺序表的数据，列表
        self.size = 0                    # 顺序表的长度

    # 0.顺序表的最大容量修改为n
    def __resize(self, n):
        assert n >= 0
        # 备份原来的数据
        a = self.data
        self.data = [None] * n
        for i in range(self.size):
            self.data[i] = a[i]
        self.capcity = n

    # 1.创建顺序表,数据源是列表a
    def create(self, a):
        for i in range(len(a)):
            if self.size == self.capcity:  # 顺序表满了，2倍扩容
                self.__resize(self.capcity * 2)
            self.data[i] = a[i]
            self.size += 1

    # 2.输出顺序表
    def print(self):
        print("顺序表的长度是：", self.size)
        print("顺序表的元素是：", *self.data[:self.size])

    # 3.1根据序号i查找
    def findIndex(self, i):
        if 0 <= i < self.size:
            return self.data[i]
        else:
            return "Index out of range"

    # 3.2查找x
    def find(self, x):
        for i in range(self.size):
            if self.data[i] == x:
                return i
        return -1

    # 4.修改序号i的元素为x
    def set(self, i, x):
        if 0 <= i < self.size:
            self.data[i] = x
        else:
            return "Index out of range"

    # 5.在序号i前插入x
    def insert(self, i, x):
        # 异常情况
        assert 0 <= i <= self.size
        if self.size == self.capcity:
            self.__resize(2 * self.capcity)
        # 序号i开始依次依次后移，从后到前
        for j in range(self.size, i, -1):
            self.data[j] = self.data[j - 1]
        self.data[i] = x
        self.size += 1

    # 6.删除序号i的元素
    def erase(self, i):
        if 0 <= i < self.size:
            for j in range(i, self.size - 1):
                self.data[j] = self.data[j + 1]
            self.data[self.size - 1] = None
            self.size -= 1
        else:
            return "Index out of range"

    # 7.排序
    def sort(self):
        self.data[:self.size] = sorted(self.data[:self.size])

    # 8.有序表的插入
    def insertSorted(self, x):
        if self.size == self.capcity:
            self.__resize(2 * self.capcity)
        i = 0
        while i < self.size and self.data[i] < x:
            i += 1
        self.insert(i, x)

# 合并2个有序表a和b
def mergeSorted(a, b):
    c = SqList()        # 创建新表c
    # 定义3个指针i，j和k，分别指向表a，表b和表c
    i = j = k = 0
    # i和j都在表的有效范围内,比较a[i]和b[j],选择小的放入新表
    while i < a.size and j < b.size:
        if a.findIndex(i) < b.findIndex(j):
            c.insert(k, a.findIndex(i))
            i += 1
        else:
            c.insert(k, b.findIndex(j))
            j += 1
        k += 1
    # 没取完的依次放入新表
    while i < a.size:
        c.insert(k, a.findIndex(i))
        i += 1
        k += 1
    while j < b.size:
        c.insert(k, b.findIndex(j))
        j += 1
        k += 1
    return c

# 测试程序
sq = SqList()
sq.create([1, 2, 3, 4, 5])
sq.print()
sq.insert(0, 6)
sq.print()

print("查找元素3的位置:", sq.find(3))
sq.erase(2)
sq.print()
sq.set(2, 10)
sq.print()
sq.sort()
sq.print()
sq.insertSorted(7)
sq.print()

## 测试程序
a = SqList()
b = SqList()
a.create([1, 3, 5, 7])
b.create([2, 4, 6, 8])
c = mergeSorted(a, b)
c.print()
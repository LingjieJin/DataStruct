class SqList:  
    def __init__(self):  
        self.init_capacity = 1000  # 假设最大容量为1000  
        self.data = [None] * self.init_capacity  # 初始化顺序表  
        self.size = 0  # 当前顺序表的大小  

    # 创建顺序表的方法  
    def create(self, elements):  
        for element in elements:  
            self.data[self.size] = element  
            self.size += 1  

    # 插入一个元素，同时保持顺序表的有序性  
    def insert(self, x):  
        # 确认顺序表是否已满  
        if self.size >= self.init_capacity:  
            return False  
        
        # 查找插入位置  
        pos = 0  
        while pos < self.size and self.data[pos] <= x:  
            pos += 1  
        
        # 将后面的元素后移  
        for j in range(self.size, pos, -1):  
            self.data[j] = self.data[j - 1]  
        
        # 插入元素x  
        self.data[pos] = x  
        self.size += 1  # 更新大小  
        return True  

    # 打印顺序表的元素  
    def print(self):  
        print(" ".join(map(str, self.data[:self.size])) + " ")


sq = SqList()  # 创建顺序表  
length = int(input().strip())  # 输入顺序表的长度  
elements = list(map(int, input().strip().split()))  # 输入顺序表的元素  
x = int(input().strip())  # 输入要插入的元素  
    
sq.create(elements)  # 根据元素创建顺序表  
sq.insert(x)  # 插入新元素  
sq.print()  # 打印更新后的顺序表
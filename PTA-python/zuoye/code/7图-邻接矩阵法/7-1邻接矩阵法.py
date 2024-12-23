class adjMatrixGraph:
    # 构造方法，n个点m条边,dir无向图标记（默认无向图），w带权标记（默认带权图）
    def __init__(self, n, m, dir=False, w=True):
        self.verNum = n  # 顶点数
        self.edgeNum = m  # 边数
        self.dir, self.wt = dir, w  # 无向图标记和带权标记
        self.vertex = [0] * n  # 顶点列表
        self.edge = [[0 if self.wt else float('inf') for i in range(self.verNum)] for j in range(self.verNum)]  # 边列表

    def print(self):  # 输出图，邻接矩阵注意输出格式
        print("顶点数：%d,边数:%d" % (self.verNum, self.edgeNum))
        print("顶点:", self.vertex)
        print("边:")
        for row in self.edge:
            print(row)

    def addVertex(self, ls):  # 添加点
        self.vertex = ls

    def addEdge(self, fr, to, w=1):  # 添加边，(fr,to)边权是w
        ifr = self.vertex.index(fr)  # 起点下标
        ito = self.vertex.index(to)  # 终点下标
        if self.dir:  # 有向图
            self.edge[ifr][ito] = w
        else:  # 无向图
            self.edge[ifr][ito] = self.edge[ito][ifr] = w

    # 求度数
    def printDegree(self):
        if self.dir:# 有向图
            in_degrees = [0] * self.verNum
            out_degrees = [0] * self.verNum
            for i in range(self.verNum):
                for j in range(self.verNum):
                    if self.edge[i][j] != 0 and self.edge[i][j] != float('inf'):
                        out_degrees[i] += 1
                        in_degrees[j] += 1
            for i in range(self.verNum):
                print(f"{self.vertex[i]}的入度: {in_degrees[i]}, 出度: {out_degrees[i]}, 度数: {in_degrees[i] + out_degrees[i]}")
        else:
            degrees = [0] * self.verNum
            for i in range(self.verNum):
                for j in range(self.verNum):
                    if self.edge[i][j] != 0 and self.edge[i][j] != float('inf'):
                        degrees[i] += 1
            for i in range(self.verNum):
                print(f"{self.vertex[i]}的度数: {degrees[i]}")

# 测试程序 
def test1_1():
    # 无向图
    print("无向图1测试")
    g = adjMatrixGraph(4, 6, False, False)
    g.addVertex(list("v1 v2 v3 v4".split()))
    g.addEdge("v1", "v2")
    g.addEdge("v1", "v3")
    g.addEdge("v1", "v4")
    g.addEdge("v2", "v3")
    g.addEdge("v2", "v4")
    g.addEdge("v3", "v4")
    g.print()
    g.printDegree()

def test1_2():
    # 无向图
    print("无向图2测试")
    g = adjMatrixGraph(5, 5, False, False)
    g.addVertex(list("v1 v2 v3 v4 v5".split()))
    g.addEdge("v1", "v2")
    g.addEdge("v1", "v3")
    g.addEdge("v2", "v4")
    g.addEdge("v3", "v5")
    g.addEdge("v4", "v5")
    g.print()
    g.printDegree()

def test2_1():
    # 有向图
    print("有向图1测试")
    g = adjMatrixGraph(4, 6, True, False)
    g.addVertex(list("v1 v2 v3 v4".split()))
    g.addEdge("v1", "v2")
    g.addEdge("v1", "v3")
    g.addEdge("v1", "v4")
    g.addEdge("v2", "v3")
    g.addEdge("v2", "v4")
    g.addEdge("v3", "v4")
    g.print()
    g.printDegree()

def test2_2():
    # 有向图
    print("有向图2测试")
    g = adjMatrixGraph(5, 5, True, False)
    g.addVertex(list("v1 v2 v3 v4 v5".split()))
    g.addEdge("v1", "v2")
    g.addEdge("v1", "v3")
    g.addEdge("v2", "v4")
    g.addEdge("v3", "v5")
    g.addEdge("v4", "v5")
    g.print()
    g.printDegree()
def test3():
    # 带权图
    print("带权图测试")
    g = adjMatrixGraph(6, 9, True, True)
    g.addVertex(list("v0 v1 v2 v3 v4 v5".split()))
    g.addEdge("v0", "v1", 5)
    g.addEdge("v0", "v5", 2)
    g.addEdge("v1", "v2", 4)
    g.addEdge("v2", "v3", 9)
    g.addEdge("v3", "v4", 7)
    g.addEdge("v3", "v5", 3)
    g.addEdge("v4", "v0", 1)
    g.addEdge("v5", "v2", 1)
    g.addEdge("v5", "v4", 8)
    g.print()
    g.printDegree()

# 获取输入
test1_1()
test1_2()
test2_1()
test2_2()
test3()
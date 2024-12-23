from collections import deque

class Vertex:
    def __init__(self, num):
        self.id = num
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0
        self.vis = set()  # 顶点访问集

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertices

    # 添加邻接边，f-from起点 t-to终点,cost-边权
    def addEdge(self, f, t, cost=0):
        if f not in self.vertices:  # 起点f不存在添加起点f
            nv = self.addVertex(f)
        if t not in self.vertices:  # 终点t不存在添加终点t
            nv = self.addVertex(t)
        # 顶点f的邻接表添加邻接边
        self.vertices[f].addNeighbor(self.vertices[t], cost)

    def getVertices(self):
        return list(self.vertices.keys())

    # 输出邻接表
    def print(self):
        for i in self.vertices.keys():
            v = self.vertices[i]  # 邻接点
            print(v.id, end="")
            for j in v.connectedTo.keys():
                print("->", j.id, end="")
            print()

    # 计算图的度数（有向图还需要计算入度和出度）
    def calculateDegrees(self):
        degrees = {key: {"in": 0, "out": 0} for key in self.vertices.keys()}
        for v in self.vertices.values():
            for nbr in v.connectedTo.keys():
                degrees[v.id]["out"] += 1
                degrees[nbr.id]["in"] += 1
        return degrees

    # 深度优先遍历，从顶点st（名称，字符串类型）出发搜到的连通分量
    def dfs(self, st, d):
        self.vis.add(st)  # 标记当前顶点st已访问
        if d > 1:  # 边界条件，第1个点前没有逗号
            print(",", end="")
        print(st, end="")  # 输出当前顶点
        # 遍历st的所有邻接边
        for v in self.vertices[st].connectedTo.keys():
            # 当前顶点没访问过
            if v.id not in self.vis:
                self.dfs(v.id, d + 1)  # 递归访问顶点i

    # 深度优先遍历，从顶点st出发搜到的所有点
    def dfsAll(self, st):
        self.vis = set()  # 初始化访问列表
        ls = list(range(st, self.numVertices)) + list(range(0, st))  # 拼接顶点列表
        for i in ls:  # 遍历所有顶点
            if i not in self.vis:  # 如果顶点i没有访问过
                self.dfs(i, 1)  # 深搜顶点i出发的连通分量
                print()

    # 广度优先遍历，从顶点st出发搜到的连通分量
    def bfs(self, st):
        # 0.初始化，定义队列，顶点的访问列表
        q = deque()
        vis = set()
        # 1.出发点入队并标记访问过
        q.append(st)
        vis.add(st)
        # 2.只要队列非空，进入队列循环
        while q:
            # 2.1出队并输出当前顶点vt
            vt = q.popleft()
            print(vt, end=",")
            # 2.2遍历邻接表
            for v in self.vertices[vt].connectedTo.keys():
                # vt的邻接点v只要没访问过就入队
                if v.id not in vis:
                    q.append(v.id)
                    vis.add(v.id)

# 测试程序
# sample
# g = Graph()
# g.addEdge('v1', 'v2')
# g.addEdge('v2', 'v1')
# g.addEdge('v2', 'v3')
# g.addEdge('v3', 'v2')
# g.addEdge('v3', 'v4')
# g.addEdge('v4', 'v3')
# g.addEdge('v4', 'v1')
# g.addEdge('v1', 'v4')
# g.print()

# # sample1
# g = Graph()
# g.addEdge('v1', 'v2')
# g.addEdge('v2', 'v3')
# g.addEdge('v3', 'v4')
# g.addEdge('v4', 'v1')
# g.print()

# sample1
g = Graph()
g.addEdge('v1', 'v2')
g.addEdge('v2', 'v3')
g.addEdge('v3', 'v4')
g.addEdge('v4', 'v1')
g.print()

print("深度优先遍历：", end="")
g.dfs("v1", 1)
print("\n广度优先遍历：", end="")
g.bfs("v1")

# 计算图的度数
degrees = g.calculateDegrees()
print("\n图的度数：")
for vertex, degree in degrees.items():
    print(f"{vertex}: in-degree = {degree['in']}, out-degree = {degree['out']}")
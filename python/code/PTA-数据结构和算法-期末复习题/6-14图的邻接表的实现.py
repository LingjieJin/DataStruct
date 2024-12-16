class arcnode:
    def __init__(self,adjvex,weight,link=None):
        self.adjvex = adjvex
        self.weight = weight
        self.link=link

class vexnode:
    def __init__(self,data,first_arc=None):
        self.data = data
        self.first_arc = first_arc

class Graph:
    def __init__(self):
        self.vex_list=[]
        self.vex_num=0
        self.edge_num=0
    
    def addVertex(self, vex_val):  
        # 添加顶点并创建对应的邻接表节点  
        new_vertex = vexnode(vex_val)  
        self.vex_list.append(new_vertex)  
        self.vex_num += 1 

    def addEdge(self, f, t, cost=0):  
        # 添加边，f 和 t 是顶点的索引  
        # 将 t 添加到 f 的邻接表中  
        new_arc = arcnode(t, cost)  
        new_arc.link = self.vex_list[f].first_arc  
        self.vex_list[f].first_arc = new_arc  
        
        # 如果是无向图，还需要将 f 添加到 t 的邻接表中  
        new_arc_reverse = arcnode(f, cost)  
        new_arc_reverse.link = self.vex_list[t].first_arc  
        self.vex_list[t].first_arc = new_arc_reverse  
        
        self.edge_num += 1 
     
     
    def print_graph(self):
        for i in range(self.vex_num):
            print(self.vex_list[i].data,end="->")
            cur = self.vex_list[i].first_arc
            while cur:
                print("adj:{},weight:{}".format(cur.adjvex,cur.weight),end="->")
                cur = cur.link
            print('None')

if __name__ =="__main__":
    g = Graph()
    s =input()
    for vertex in s:
        g.addVertex(vertex)

    g.addEdge(0,1,11)
    g.addEdge(0,2,55)
    g.addEdge(2,3,88)
    g.addEdge(0,3,33)
    g.addEdge(1,2,44)
    g.print_graph()
"""
本题要求输出两个顶点之间是否存在路径

输入格式:
输入包括两部分，第一部分是邻接矩阵表示方法中对应1的两个顶点，用0 0 表示结束
第二部分是两个顶点，例如 Vi和Vj

输出格式:
如果Vi和Vj存在路径，输出1；否则输出0

输入样例:
0 1
1 0
0 4
4 0
1 4
4 1
1 2
2 1
1 3
3 1
2 3
3 2
4 5
5 4
4 6
6 4
0 0
0 5
输出样例:
1
"""


def dfs(graph, visited, v, target):  
    """深度优先搜索，判断从 v 到 target 是否存在路径"""  
    if v == target:  
        return True  
    visited[v] = True  # 标记当前节点为已访问  
    for i in range(len(graph)):  
        if graph[v][i] == 1 and not visited[i]:  # 如果存在边且未被访问  
            if dfs(graph, visited, i, target):  # 递归DFS  
                return True  
    return False  

def main():  
    # 读取邻接矩阵  
    edges = []  
    while True:  
        line = input().strip()  
        u, v = map(int, line.split())  
        if u == 0 and v == 0:  
            break  
        edges.append((u, v))  
    
    
    max_vertex = 7  
    graph = [[0] * max_vertex for _ in range(max_vertex)]  

    # 填充邻接矩阵  
    for u, v in edges:  
        graph[u][v] = 1  # 有向边 u -> v  

    # 读取要查询的两个顶点  
    line = input().strip()  
    vi, vj = map(int, line.split())  

    # 初始化访问数组  
    visited = [False] * max_vertex  

    # 判断路径是否存在  
    if dfs(graph, visited, vi, vj):  
        print(1)  
    else:  
        print(0)  

if __name__ == "__main__":  
    main()
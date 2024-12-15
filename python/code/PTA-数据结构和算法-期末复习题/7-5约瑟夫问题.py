"""
约瑟夫问题：有ｎ只猴子，按顺时针方向围成一圈选大王（编号从１到ｎ），从第１号开始报数，一直数到ｍ，数到ｍ的猴子退出圈外，剩下的猴子再接着从1开始报数。就这样，直到圈内只剩下一只猴子时，这个猴子就是猴王，编程求输入ｎ，ｍ后，输出最后猴王的编号。

输入格式:
每行是用空格分开的两个整数，第一个是 n, 第二个是 m ( 0 < m,n <=300)。最后一行是：

0 0

输出格式:
对于每行输入数据（最后一行除外)，输出数据也是一行，即最后猴王的编号

输入样例:
6 2
12 4
8 3
0 0
输出样例:
5
1
7
"""

def josephus(n, m):  
    """约瑟夫问题模拟"""  
    # 初始设定：构建猴子的列表  
    monkeys = list(range(1, n + 1))  # 猴子的编号从1到n  
    
    index = 0  # 当前报数的猴子索引  
    
    while len(monkeys) > 1:  # 直到只剩一个猴子  
        index = (index + m - 1) % len(monkeys)  # 计算出局的猴子索引  
        monkeys.pop(index)  # 移除这个猴子  
    
    return monkeys[0]  # 返回最后剩下的猴子编号  

if __name__ == "__main__":  
    while True:  
        # 读取输入  
        line = input().strip()  
        n, m = map(int, line.split())  
        
        if n == 0 and m == 0:  # 如果输入是 "0 0"，则结束程序  
            break  
        
        # 计算最后猴王的编号并输出  
        result = josephus(n, m)  
        print(result)
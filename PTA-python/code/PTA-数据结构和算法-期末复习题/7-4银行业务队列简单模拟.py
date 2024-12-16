"""
设某银行有A、B两个业务窗口，且处理业务的速度不一样，其中A窗口处理速度是B窗口的2倍 —— 即当A窗口每处理完2个顾客时，B窗口处理完1个顾客。给定到达银行的顾客序列，请按业务完成的顺序输出顾客序列。假定不考虑顾客先后到达的时间间隔，并且当不同窗口同时处理完2个顾客时，A窗口顾客优先输出。

输入格式:
输入为一行正整数，其中第1个数字N(≤1000)为顾客总数，后面跟着N位顾客的编号。编号为奇数的顾客需要到A窗口办理业务，为偶数的顾客则去B窗口。数字间以空格分隔。

输出格式:
按业务处理完成的顺序输出顾客的编号。数字间以空格分隔，但最后一个编号后不能有多余的空格。

输入样例:
8 2 1 3 9 4 11 13 15
输出样例:
1 3 2 9 11 4 13 15
"""


from collections import deque  

def process_customers(customers):  
    """处理顾客队列并返回完成的顾客顺序"""  
    queue_a = deque()  # A窗口的顾客队列  
    queue_b = deque()  # B窗口的顾客队列  
    result = []  # 存储处理完成的顾客顺序  

    # 将顾客分配到对应的窗口队列  
    for customer in customers:  
        if customer % 2 == 1:  # 奇数顾客到A窗口  
            queue_a.append(customer)  
        else:  # 偶数顾客到B窗口  
            queue_b.append(customer)  

    # 模拟处理顾客  
    while queue_a or queue_b:  
        # A窗口每次处理2个顾客  
        if len(queue_a) >= 2:  
            result.append(queue_a.popleft())  
            result.append(queue_a.popleft())  
        elif queue_a:  # 如果剩下1个顾客  
            result.append(queue_a.popleft())  

        # B窗口每次处理1个顾客  
        if queue_b:  
            result.append(queue_b.popleft())  

    return result  

if __name__ == "__main__":  
    # 读取输入  
    input_data = input().strip().split()  
    n = int(input_data[0])  # 顾客总数  
    customers = list(map(int, input_data[1:n+1]))  # 顾客编号  

    # 处理顾客并获取完成顺序  
    completed_customers = process_customers(customers)  

    # 输出结果  
    print(" ".join(map(str, completed_customers)))
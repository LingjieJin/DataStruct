def josephus(n):  
    """解决约瑟夫环问题"""  
    people = list(range(1, n + 1))  # 创建一个列表，包含从1到n的所有人  
    index = 0  # 从第一个人开始  

    while len(people) > 1:  
        # 找到下一个要退出的人，index + 2（因为要报到3出局）  
        index = (index + 2) % len(people)  # 每次报数2，得到3的就是需要出局的人  
        people.pop(index)  # 移除此人  

    return people[0]  # 返回最后剩下的人的编号  

if __name__ == '__main__':  
    import sys  

    results = []  # 用于存储所有结果  

    try:  
        while True:  # 无限循环以处理多组输入  
            n = int(input().strip())  # 逐行读取输入  
            results.append(josephus(n))  # 计算并将结果存储在列表中  
    except EOFError:  
        # 当读取到文件末尾时，结束输入并直接退出程序  
        pass  # 直接跳到输出步骤  

    # 输出所有结果，每个结果之间用换行分隔，且最后没有换行  
    print("\n".join(map(str, results)))  
    sys.exit()  # 直接退出程序
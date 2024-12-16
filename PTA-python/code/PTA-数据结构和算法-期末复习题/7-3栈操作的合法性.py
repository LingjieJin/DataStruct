"""
假设以S和X分别表示入栈和出栈操作。如果根据一个仅由S和X构成的序列，对一个空堆栈进行操作，相应操作均可行（如没有出现删除时栈空）且最后状态也是栈空，则称该序列是合法的堆栈操作序列。请编写程序，输入S和X序列，判断该序列是否合法。

输入格式:
输入第一行给出两个正整数 n 和 m，其中 n 是待测序列的个数，m（≤50）是堆栈的最大容量。随后 n 行，每行中给出一个仅由S和X构成的序列。序列保证不为空，且长度不超过100。

输出格式:
对每个序列，在一行中输出YES如果该序列是合法的堆栈操作序列，或NO如果不是。

输入样例：
4 10
SSSXXSXXSX
SSSXXSXXS
SSSSSSSSSSXSSXXXXXXXXXXX
SSSXXSXXX
输出样例：
YES
NO
NO
NO
"""

def is_valid_stack_sequence(sequence, max_capacity):  
    """判断给定的堆栈操作序列是否合法"""  
    stack_size = 0  # 当前堆栈的大小  

    for operation in sequence:  
        if operation == 'S':  # 入栈操作  
            stack_size += 1  
            # 检查是否超过最大容量  
            if stack_size > max_capacity:  
                return "NO"  
        elif operation == 'X':  # 出栈操作  
            stack_size -= 1  
            # 检查出栈时栈是否为空  
            if stack_size < 0:  
                return "NO"  

    # 检查最后栈是否为空  
    return "YES" if stack_size == 0 else "NO"  

if __name__ == "__main__":  
    # 读取输入的n和m  
    n, m = map(int, input().strip().split())  
    
    results = []  
    
    # 读取n行序列进行判断  
    for _ in range(n):  
        sequence = input().strip()  
        result = is_valid_stack_sequence(sequence, m)  
        results.append(result)  
    
    # 输出每个序列的结果  
    for i in results:
        print(i)
"""
请设计一个能够将有序顺序表LA，LB进行合并的算法，要求合并后的顺序表LC依然有序。

例如：
LA的元素  1 3 5 7
LB的元素  2 4
LC的元素  1 2 3 4 5 7
其中，LA和LB的长度不超过1000，当中的元素为非递减排序。

输入格式:
第一行输入LA的长度

第二行输入LA的元素

第三行输入LB的长度

第四行输入LB的元素

输出格式:
输入合并后顺序表中各元素的值，值之间用一个空格间隔。

输入样例1:
4
1 3 5 7
2
2 4
输出样例1:
1 2 3 4 5 7 
输入样例2:
6
1 2 3 4 5 6
3
7 8 9
输出样例2:
1 2 3 4 5 6 7 8 9 
"""


def merge_sorted_lists(len_A, list_A, len_B, list_B):  
    # 初始化合并后顺序表  
    list_C = []  
    i, j = 0, 0  
    
    # 合并两个有序列表  
    while i < len_A and j < len_B:  
        if list_A[i] < list_B[j]:  # 使用 < 避免重复元素  
            list_C.append(list_A[i])  
            i += 1  
        elif list_A[i] > list_B[j]:  
            list_C.append(list_B[j])  
            j += 1  
        else:  # 如果相等，只添加一个  
            list_C.append(list_A[i])  
            i += 1  
            j += 1  
            
    # 如果有剩余元素，将其添加到合并列表中  
    while i < len_A:  
        list_C.append(list_A[i])  
        i += 1  
    while j < len_B:  
        list_C.append(list_B[j])  
        j += 1  
        
    return list_C  

# 输入格式  
len_A = int(input())  
list_A = list(map(int, input().split())) if len_A > 0 else []  
len_B = int(input())  
list_B = list(map(int, input().split())) if len_B > 0 else []  

# 合并并输出  
list_C = merge_sorted_lists(len_A, list_A, len_B, list_B)  
print(' '.join(map(str, list_C))+" ")
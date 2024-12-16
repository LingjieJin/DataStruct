"""
输入格式:
输入在第1行中给出N（1<N≤100），在第2行中给出N个待排序的整数，数字间以空格分隔，并保证数字没有重复的出现。

输出格式:
给出选择排序每一遍后的中间结果数列，数字间以空格分隔，但末尾不得有多余空格。注意：当排序完成时应立即停止。

输入样例1:
7
4 5 7 6 3 2 1
输出样例1:
1 5 7 6 3 2 4
1 2 7 6 3 5 4
1 2 3 6 7 5 4
1 2 3 4 7 5 6
1 2 3 4 5 7 6
1 2 3 4 5 6 7
输入样例2:
5
1 2 3 5 4
输出样例2:
1 2 3 4 5
"""

def selection_sort(arr):  
    n = len(arr)  
    for i in range(n):  
        min_index = i  
        
        # 查找未排序部分的最小元素  
        for j in range(i + 1, n):  
            if arr[j] < arr[min_index]:  
                min_index = j  
        
        # 只有当最小值的索引改变时才进行交换  
        if min_index != i:  
            arr[i], arr[min_index] = arr[min_index], arr[i]  
            # 输出当前数组状态  
            print(" ".join(map(str, arr)))  

if __name__ == "__main__":  
    # 读取输入  
    n = int(input().strip())  
    arr = list(map(int, input().strip().split()))  
    
    # 执行选择排序并输出结果  
    selection_sort(arr)  

    # 如果最后一个元素未打印（完全排序完成），输出最终排序结果  
    if arr != sorted(arr):  
        print(" ".join(map(str, arr)))  
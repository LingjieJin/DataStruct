def merge_sorted_lists(len_a, list_a, len_b, list_b):  
    """合并两个有序顺序表并返回一个新的有序顺序表"""  
    list_c = []  # 用于存储合并后的有序列表  
    i, j = 0, 0  # 初始化指针  

    # 使用双指针法合并两个有序列表  
    while i < len_a and j < len_b:  
        if list_a[i] < list_b[j]:  
            list_c.append(list_a[i])  
            i += 1  
        else:  
            list_c.append(list_b[j])  
            j += 1  

    # 如果还有剩余的元素，直接添加到合并列表  
    while i < len_a:  
        list_c.append(list_a[i])  
        i += 1  
    while j < len_b:  
        list_c.append(list_b[j])  
        j += 1  

    return list_c  


if __name__ == "__main__":  
    # 输入LA的长度  
    len_a = int(input().strip())  
    # 输入LA的元素  
    list_a = list(map(int, input().strip().split()))  
    # 输入LB的长度  
    len_b = int(input().strip())  
    # 输入LB的元素  
    list_b = list(map(int, input().strip().split()))  

    # 合并两个有序列表  
    merged_list = merge_sorted_lists(len_a, list_a, len_b, list_b)  

    # 输出合并后的有序列表  
    print(" ".join(map(str, merged_list)) + " ")
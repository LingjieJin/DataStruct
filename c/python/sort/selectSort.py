# 选择排序
## 选择排序就是每次选出最小（大）的值放到排序位置前方
## 选择排序的时间复杂度是O(N^2),是不稳定排序法
def selectSort(a):
    n = len(a)
    for i in range(n - 1):
        # k记录最小值的下标
        k = i
        ## 遍历排序数组，找到最小值的下标
        for j in range(i + 1,n):
            if a[j] < a[k]:
                k = j
        if k != i:  # 自身不交换
            ## 交换最小值到本次排序最前面
            a[i],a[k] = a[k],a[i]
            
        ## 输出本次排序结果
        print("第{:^3d}次排序:".format(i + 1),*a)

if __name__ == '__main__':
    a = [49, 38, 97, 76, 65, 13, 27, 50]
    selectSort(a)
    print("排序后的结果:" *a)

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = Node()
        self.head.next = None

    def createByTail(self, a):
        tail = self.head
        for i in range(len(a)):
            p = Node(a[i])
            tail.next = p
            tail = p
        tail.next = None

    def showLinkList(self):
        p = self.head.next
        while p is not None:
            print(p.data, end=" ")
            p = p.next
        print()

    def findi(self, i):
        p = self.head.next
        j = 1
        while p is not None and j < i:
            j += 1
            p = p.next
        return p

    ## 你的答案将被填在这里，请注意函数前面有4个前导空格##
    def length(self):
        p = self.head.next
        counts = 0
        while p is not None:
            counts += 1
            p = p.next
        return counts

    def addi(self, i, e):  
            # i必须在 [1, n+1] 的范围内才是合法的  
            if i < 1:  
                return False  
            
            # 创建一个新的节点  
            new_node = Node(e)  
            p = self.head  # 从头结点开始  
    
            # 找到插入位置的前一个节点  
            for j in range(1, i):  
                p = p.next  
                if p is None:  # 如果到达链表末尾且还未到达位置i，说明插入失败  
                    return False  
            
            new_node.next = p.next  # 新节点指向当前位置的下一个节点  
            p.next = new_node  # 将前一个节点的next指向新的节点  
            return True  # 插入成功 

if __name__ == '__main__':
    l = LinkList()
    n = int(input())
    a = list(map(int,input().split()))
    l.createByTail(a)
    b = list(map(int,input().split()))
    if l.addi(b[0], b[1]) is True:
        l.showLinkList()
    else:
        print("insert fail")
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
        if i < 0:
            return None
        j = 1
        while p is not None and j < i:
            j += 1
            p = p.next
        return p
    
    ## 你的答案将被填在这里，请注意函数前面有4个前导空格##
    def deletei(self, i):  
            # i必须在 [1, n] 的范围内才是合法的  
            if i < 1:  
                return False  
            
            p = self.head  # 从头节点开始  
            
            # 找到要删除节点的前一个节点  
            for j in range(1, i):  
                p = p.next  
                if p is None or p.next is None:  # 如果链表长度不够  
                    return False  
            
            # p.next 是要被删除的节点  
            node_to_delete = p.next  
            if node_to_delete is not None:  
                p.next = node_to_delete.next  # 跳过要删除的节点  
                return True  # 删除成功  
            else:  
                return False  # 如果要删除的节点不存在

if __name__ == '__main__':
    l = LinkList()
    n = int(input())
    a = list(map(int,input().split()))
    l.createByTail(a)
    i = int(input())
    if l.deletei(i) is True:
        l.showLinkList()
    else:
        print("delete fail")
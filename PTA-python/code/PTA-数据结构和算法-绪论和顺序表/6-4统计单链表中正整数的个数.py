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

    ## 你的答案将被填在这里，请注意函数前面有4个前导空格##
    def count(self):
        p = self.head.next
        counts = 0
        while p is not None:
            if p.data > 0:
                counts += 1
            p = p.next

        return counts
        
    def showLinkList(self):
        p = self.head.next
        while p is not None:
            print(p.data, end=" ")
            p = p.next
        print()
    

if __name__ == '__main__':
    l = LinkList()
    a = [eval(x) for x in input().split()]
    l.createByTail(a)
    num = l.count()
    print(num)


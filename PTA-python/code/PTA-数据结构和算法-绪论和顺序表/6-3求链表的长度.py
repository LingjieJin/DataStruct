class LinkNode:
    def __init__(self,x = None):
        self.data = x        #数据域
        self.next = None     #指针域初始化为空
#单链表类
class LinkList:
    #0.构造方法
    def __init__(self):
        self.head = LinkNode()  #创建一个带头结点
    #1.输出单链表
    def print(self):
        p = self.head.next  #p指向链表的第一个有效结点
        if p is None:
            print("空链表")
        else:
            while p.next is not None:
                print(p.data,"->",sep = "",end = "")
                p = p.next
            print(p.data)
    #2.创建单链表-尾插法
    def createTail(self,a):
        tail = self.head   #p指向链表的带头结点
        #遍历列表a
        for x in a:
            #根据x创建新结点
            p = LinkNode(x)
            #新结点p链接到链表的尾部
            tail.next = p
            tail = p
    #3.创建单链表-头插法
    def createHead(self,a):
        for x in a:
            p = LinkNode(x)
            p.next = self.head.next
            self.head.next = p
    #4.你的代码将被嵌在这里，注意整个方法的代码都要缩进4个空格（类里面的方法）
    def length(self):
        p = self.head
        size = 0
        while p.next is not None:
            size += 1
            p = p.next
        return size
    
h = LinkList()   #创建链表
a = list(map(int,input().split())) #输入数据到列表a
h.createTail(a)     #尾插法创建单链表
print(h.length())   #输出链表的长度
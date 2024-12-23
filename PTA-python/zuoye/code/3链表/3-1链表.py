# 单链表的结点（数据域和指针域）
class LinkNode:
    def __init__(self, x=None):
        self.data = x        # 数据域
        self.next = None     # 指针域初始化为空

# 单链表类
class LinkList:
    # 0.构造方法
    def __init__(self):
        self.head = LinkNode()  # 创建一个带头结点

    # 1.输出单链表
    def print(self):
        p = self.head.next  # p指向链表的第一个有效结点
        if p is None:
            print("空链表")
        else:
            while p.next is not None:
                print(p.data, "->", sep="", end="")
                p = p.next
            print(p.data)

    # 2.创建单链表-尾插法
    def createTail(self, a):
        assert len(a) > 0
        tail = self.head   # p指向链表的带头结点
        # 遍历列表a
        for x in a:
            # 根据x创建新结点
            p = LinkNode(x)
            # 新结点p链接到链表的尾部
            tail.next = p
            tail = p

    # 3.创建单链表-头插法
    def createHead(self, a):
        assert len(a) > 0
        for x in a:
            p = LinkNode(x)
            p.next = self.head.next
            self.head.next = p

    # 4.查找第i个结点
    def get(self, i):
        assert i > 0
        p = self.head
        for j in range(i):
            p = p.next
            if p is None:
                print("第%d个结点不存在" % i)
                return p
        return p

    # 5.输出第i个结点数据，支持[]
    def __getitem__(self, i):
        p = self.get(i)
        if p is None:
            return None
        return p.data

    # 6.查找x是否存在，如果存在返回第一次出现的位置，否则返回-1
    def find(self, x):
        p = self.head.next
        i = 1
        while p is not None:
            if p.data == x:
                return i
            p = p.next
            i += 1
        return -1

    # 7.插入操作，在第i个结点前插入数据域为x的新结点
    def insert(self, i, x):
        # 第1个结点前插入，特判一下
        if i == 1:
            p = self.head
        # 1)找到第i-1个结点
        else:
            p = self.get(i - 1)
        if p is None:
            return False
        # 2)创建新结点，数据域为x
        q = LinkNode(x)
        # 3)插入新结点q
        q.next = p.next     # 先连
        p.next = q          # 后断
        return True

    # 8.删除操作，删除第i个结点
    def pop(self, i):
        if i == 1:
            p = self.head
        else:
            p = self.get(i - 1)
        if p is None or p.next is None:
            return False
        p.next = p.next.next
        return True

    # 9.修改操作，第i个结点的数据域修改为x
    def set(self, i, x):
        p = self.get(i)
        if p is None:
            return False
        p.data = x
        return True

    # 10.链表的长度
    def size(self):
        p = self.head.next
        length = 0
        while p is not None:
            length += 1
            p = p.next
        return length

# 主程序
def main():
    h = LinkList()
    while True:
        print("1.显示全部记录\n2.尾插法创建链表\n3.头插法创建链表\n4.查找第i个结点\n5.插入结点\n6.删除结点\n7.修改结点\n8.求链表长度\n0.退出")
        ch = int(input())
        if ch == 0:
            print("欢迎下次使用，系统即将退出！")
            break
        elif ch == 1:
            h.print()
        elif ch == 2:
            a = list(map(int, input("请输入元素，以空格分隔：").split()))
            h.createTail(a)
        elif ch == 3:
            a = list(map(int, input("请输入元素，以空格分隔：").split()))
            h.createHead(a)
        elif ch == 4:
            i = int(input("请输入结点序号："))
            print(h[i])
        elif ch == 5:
            i = int(input("请输入插入位置："))
            x = int(input("请输入插入元素："))
            h.insert(i, x)
        elif ch == 6:
            i = int(input("请输入删除位置："))
            h.pop(i)
        elif ch == 7:
            i = int(input("请输入修改位置："))
            x = int(input("请输入新元素："))
            h.set(i, x)
        elif ch == 8:
            print("链表长度为：", h.size())
        else:
            print("你的选择有误，请重新输入！")

if __name__ == "__main__":
    main()
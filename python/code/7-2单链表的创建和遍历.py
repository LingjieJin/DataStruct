class Node:  
    def __init__(self, data):  
        self.data = data  # 节点存储的数据  
        self.next = None  # 下一个节点的指针  

class SinglyLinkedList:  
    def __init__(self):  
        self.head = None  # 链表的头节点  

    def insert(self, data):  
        """在链表末尾插入一个新节点"""  
        new_node = Node(data)  
        if not self.head:  
            self.head = new_node  # 如果链表为空，直接将头指向新节点  
        else:  
            current = self.head  
            while current.next:  # 找到链表的最后一个节点  
                current = current.next  
            current.next = new_node  # 将最后节点的next指向新节点  

    def traverse(self):  
        """遍历链表并返回一个包含所有节点数据的列表"""  
        current = self.head  
        elements = []  
        while current:  # 直到当前节点为空  
            elements.append(str(current.data))  # 收集当前节点的数据  
            current = current.next  # 处理下一个节点  
        if len(elements) == 0:
            return True
        else:
            print(" ".join(elements))  # 把数据用空格连接成字符串返回  


n = int(input().strip())  # 读入n值  
values = list(map(int, input().strip().split()))  # 读入n个整数  

linked_list = SinglyLinkedList()  # 创建单链表  
if n > len(values):
    for value in values:
        linked_list.insert(value)  # 将每个整数插入链表  
else:
    for value in values[:n]:
        linked_list.insert(value)  # 将每个整数插入链表  
    
# 输出链表的元素，以空格分隔  
linked_list.traverse()
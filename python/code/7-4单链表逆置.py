class Node:  
    """链表节点类"""  
    def __init__(self, data=None):  
        self.data = data  # 节点数据  
        self.next = None  # 指向下一个节点  

class SinglyLinkedList:  
    """带头结点的单链表类"""  
    def __init__(self):  
        self.head = Node()  # 创建头结点  
        self.size = 0       # 链表大小  

    def append(self, data):  
        """在链表末尾添加新节点"""  
        new_node = Node(data)  
        current = self.head  
        
        # 找到链表的末尾  
        while current.next:  
            current = current.next  
            
        current.next = new_node  
        self.size += 1  

    def reverse(self):  
        """就地逆置链表"""  
        prev = None  
        current = self.head.next  # 从第一个节点开始  
        while current:  
            next_node = current.next  # 暂存下一个节点  
            current.next = prev       # 反转当前节点的指向  
            prev = current            # 移动prev指针  
            current = next_node       # 移动current指针  
        self.head.next = prev  # 更新头结点指向新的头  

    def print_list(self):  
        """输出链表中的数据"""  
        current = self.head.next  # 跳过头结点  
        result = []  
        while current:  
            result.append(str(current.data))  
            current = current.next  
        print(" ".join(result))  # 用空格连接节点数据并输出  

# 主程序  
if __name__ == '__main__':  
    T = int(input())  # 输入测试数据组数  
    for _ in range(T):  
        linked_list = SinglyLinkedList()  # 创建新的链表  
        data = list(map(int, input().split()))  
        
        for number in data:  
            if number == -1:  
                break  
            linked_list.append(number)  # 在链表末尾添加节点  
            
        linked_list.reverse()  # 逆置链表  
        linked_list.print_list()  # 输出逆置后的链表数据
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 创建一个哨兵节点
        dummy = ListNode()
        current = dummy
        
        # 遍历两个链表，按顺序合并
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        # 连接剩余的节点
        current.next = l1 if l1 else l2
        
        return dummy.next

# 示例测试
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
solution = Solution()
merged_list = solution.mergeTwoLists(l1, l2)
print_list(merged_list)  # 输出: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        
        # 遍历链表，删除重复元素
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head

# 示例测试
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
solution = Solution()
unique_list = solution.deleteDuplicates(head)
print_list(unique_list)  # 输出: 1 -> 2 -> 3 -> None
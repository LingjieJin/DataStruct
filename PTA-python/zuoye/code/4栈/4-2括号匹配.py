class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

def is_matching_pair(char1, char2):
    pairs = {')': '(', ']': '[', '}': '{'}
    return pairs.get(char1) == char2

def check_parentheses(expression):
    stack = LinkedStack()
    for char in expression:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty() or not is_matching_pair(char, stack.pop()):
                return "no"
    return "yes" if stack.is_empty() else "no"

# 处理多组测试数据
import sys

def main():
    input = sys.stdin.read
    data = input().strip().split('\n')

    for expression in data:
        print(check_parentheses(expression))

if __name__ == "__main__":
    main()
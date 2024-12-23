class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

def decimal_to_base(n, r):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    stack = Stack()
    result = ""

    # 将十进制数转换为r进制数
    while n > 0:
        remainder = n % r
        stack.push(digits[remainder])
        n = n // r

    # 从栈中取出转换后的r进制数
    while not stack.is_empty():
        result += stack.pop()

    return result

# 处理多组测试数据
import sys
input = sys.stdin.read
data = input().strip().split()

for i in range(0, len(data), 2):
    n = int(data[i])
    r = int(data[i + 1])
    print(decimal_to_base(n, r))
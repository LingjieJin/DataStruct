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

def evaluate_postfix(expression):
    stack = Stack()
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            stack.push(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 // operand2  # 使用整数除法
            elif token == '%':
                result = operand1 % operand2
            stack.push(result)

    return stack.pop()

# 处理多组测试数据
import sys

def main():
    input = sys.stdin.read
    data = input().strip().split('\n')

    for expression in data:
        print(evaluate_postfix(expression))

if __name__ == "__main__":
    main()
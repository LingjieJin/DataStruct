from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(a / b))  # 注意 Python 中的除法需要取整

        return stack[0]

# 示例测试
solution = Solution()
print(solution.evalRPN(["2", "1", "+", "3", "*"]))  # 输出: 9
print(solution.evalRPN(["4", "13", "5", "/", "+"]))  # 输出: 6
print(solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # 输出: 22
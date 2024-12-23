class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack

# 示例测试
solution = Solution()
print(solution.isValid("()"))  # 输出: True
print(solution.isValid("()[]{}"))  # 输出: True
print(solution.isValid("(]"))  # 输出: False
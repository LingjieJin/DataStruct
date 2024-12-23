class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 负数和以0结尾的数（除0本身外）都不是回文数
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # 反转数字的一半
        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
        
        # 当数字长度为奇数时，我们可以通过 reverted_number//10 去除中间的数字
        return x == reverted_number or x == reverted_number // 10

# 示例测试
x = 121
solution = Solution()
print(solution.isPalindrome(x))  # 输出: True

x = -121
print(solution.isPalindrome(x))  # 输出: False

x = 10
print(solution.isPalindrome(x))  # 输出: False
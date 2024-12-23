from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # 初始化两个指针
        i = 0
        for j in range(1, len(nums)):
            # 如果当前元素不等于前一个元素，则将其移动到前面
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

# 示例测试
nums = [1, 1, 2]
solution = Solution()
print(solution.removeDuplicates(nums))  # 输出: 2
print(nums)  # 输出: [1, 2, _]
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 初始化两个指针
        i = 0
        for j in range(len(nums)):
            # 如果当前元素不等于 val，则将其移动到前面
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

# 示例测试
nums = [3, 2, 2, 3]
val = 3
solution = Solution()
print(solution.removeElement(nums, val))  # 输出: 2
print(nums)  # 输出: [2, 2, _, _]
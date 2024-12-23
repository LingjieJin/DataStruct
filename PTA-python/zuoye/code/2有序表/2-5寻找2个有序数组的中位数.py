from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 合并两个有序数组
        nums = sorted(nums1 + nums2)
        n = len(nums)
        
        # 如果数组长度为奇数，返回中间元素
        if n % 2 == 1:
            return float(nums[n // 2])
        # 如果数组长度为偶数，返回中间两个元素的平均值
        else:
            return (nums[n // 2 - 1] + nums[n // 2]) / 2

# 示例测试
nums1 = [1, 3]
nums2 = [2]
solution = Solution()
print(solution.findMedianSortedArrays(nums1, nums2))  # 输出: 2.0

nums1 = [1, 2]
nums2 = [3, 4]
print(solution.findMedianSortedArrays(nums1, nums2))  # 输出: 2.5
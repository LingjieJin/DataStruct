from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 创建一个字典来存储数值和对应的索引
        num_to_index = {}
        
        # 遍历数组
        for i, num in enumerate(nums):
            # 计算目标值与当前数值的差
            complement = target - num
            
            # 如果差值在字典中，返回当前索引和差值的索引
            if complement in num_to_index:
                return [num_to_index[complement], i]
            
            # 将当前数值和索引存入字典
            num_to_index[num] = i

# 示例测试
nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))
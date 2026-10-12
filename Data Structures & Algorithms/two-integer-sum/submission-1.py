class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_hash:
                return [nums_hash[complement], i]
            nums_hash[num] = i
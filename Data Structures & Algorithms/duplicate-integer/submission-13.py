class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for index in range(1, len(nums)):
            if nums[index] == nums[index-1]:
                return True
        return False
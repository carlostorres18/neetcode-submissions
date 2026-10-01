class Solution:
    # Time complexity is O(n log n), this is because of .sort() function being called
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        return True if len(nums) != len(nums_set) else False


# 1. the problem is to check whether an array contains any duplicates and just return True if it does and False if it doesnt.

# 2. some important edge cases would have to be if its empty, and also if its unsorted

# 3. The brute force solution, would be to compare every element against every other elements, until you find the duplicates, which would be O(n^2)

# 4. One of the solutions that i found was, sorting the array with .sort() and checking for the neighbor, worst case is you would go through all N elements in the array in this case the time would be O(n log n), which is better then the brute force approach but not the optimal

# def hasDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for index in range(1, len(nums)):
#             if nums[index] == nums[index-1]:
#                 return True
#         return False

# 5. the optimal solution would be to use a set and then compare the len of the original array with the len of the size, and if they are different return True, this would make the time O(n)
# 6. 
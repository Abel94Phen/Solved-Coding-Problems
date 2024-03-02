class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        subset = []
        def backtrack(index):
            if index >= len(nums):
                result.append(subset[:])
                return
                

            subset.append(nums[index])
            backtrack(index + 1)

            subset.pop()
            while index < len(nums) - 1 and nums[index] == nums[index + 1]:
                index += 1
            backtrack(index + 1)

        backtrack(0)
        return result

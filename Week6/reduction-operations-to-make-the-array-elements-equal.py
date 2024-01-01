class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        operations = 0
        i = nums.index(max(nums))
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                operations += len(nums) - i
        return operations

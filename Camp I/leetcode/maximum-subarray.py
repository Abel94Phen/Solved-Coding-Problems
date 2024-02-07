class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        MaxSum = nums[0]
        LocalSum = MaxSum
        for i in range(1, len(nums)):
            LocalSum = max(nums[i], nums[i] + LocalSum)
            if LocalSum > MaxSum:
                MaxSum = LocalSum
        return MaxSum
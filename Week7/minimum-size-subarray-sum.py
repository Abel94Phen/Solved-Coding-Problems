class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        Sum, i, j = 0, 0, 0
        length = len(nums) + 1
        while Sum < target  and j < len(nums):
            Sum += nums[j]   
            while Sum >= target:
                length = min(length, j - i + 1)
                Sum -= nums[i]
                i += 1
            j += 1
        if length == len(nums) + 1:
            return 0
        return length
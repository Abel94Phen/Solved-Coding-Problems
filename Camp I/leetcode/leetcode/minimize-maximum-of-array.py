class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix_sum = nums[0]
        max_int = prefix_sum
        for i in range(1, len(nums)):
            prefix_sum += nums[i]
            max_int = max(max_int, ceil(prefix_sum/(i + 1)))
        return max_int
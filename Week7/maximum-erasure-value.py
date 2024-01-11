class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        l = 0
        max_sum, Sum = 0, 0
        j = 0
        for i in range(len(nums)):
            while nums[i] in seen:
                Sum-= nums[j]
                seen.remove(nums[j])
                j += 1
            Sum += nums[i]
            seen.add(nums[i])
            max_sum = max(max_sum, Sum)
        return max_sum            
            
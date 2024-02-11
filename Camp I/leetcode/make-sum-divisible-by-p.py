class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remainder = sum(nums)%p
        if not remainder:
            return 0 
        
        hashmap = {0:-1}
        min_length = len(nums) + 1
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            target = ((prefix_sum % p) - remainder)%p
            hashmap[prefix_sum % p] = i

            if target in hashmap:
                min_length = min(min_length, i - hashmap[target])
        
        return min_length if min_length != len(nums) + 1 and min_length != len(nums) else -1
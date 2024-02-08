class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # [1,1,2,2,3]
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        hashmap = {0:1}

        subarray_count = 0

        for right in range(len(nums)):
            left_sum = nums[right] - goal
            subarray_count += hashmap.get(left_sum, 0) 
            hashmap[nums[right]] = hashmap.get(nums[right], 0) + 1
                 
        return subarray_count


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarray_count = 0
        subarray_sum = 0
        prefix_sums = {0:1}

        for num in nums:
            subarray_sum += num
            prefix = subarray_sum - k
            
            subarray_count += prefix_sums.get(prefix, 0)
            prefix_sums[subarray_sum] = prefix_sums.get(subarray_sum, 0) + 1
        return subarray_count
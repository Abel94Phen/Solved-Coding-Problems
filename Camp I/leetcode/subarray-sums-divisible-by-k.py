class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        divisible_count = 0
        subarray_sum = 0
        prefix_sums = {0:1}

        for num in nums:
            subarray_sum += num
            mod = subarray_sum%k
            divisible_count += prefix_sums.get(mod, 0)
            prefix_sums[mod] = prefix_sums.get(mod, 0) + 1
        return divisible_count
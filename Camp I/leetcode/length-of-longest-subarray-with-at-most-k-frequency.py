class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hashmap = {}
        Max_len = 0
        left = 0
        for right in range(len(nums)):
            hashmap[nums[right]] = 1 + hashmap.get(nums[right], 0)
            while hashmap[nums[right]] > k:
                hashmap[nums[left]] -= 1
                if hashmap[nums[left]] == 0:
                    del hashmap[nums[left]]
                left += 1
            Max_len = max(Max_len, right - left + 1)
        return Max_len

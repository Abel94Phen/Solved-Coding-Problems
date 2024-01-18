class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_length = 0
        left = 0
        zeros = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_length = max(max_length, right - left + 1 - zeros)
        return max_length - 1 if max_length == len(nums) else max_length
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0
        for i in nums:
            if i-1 not in numbers:
                length = 0
                while i + length in numbers:
                    length += 1
                longest = max(longest, length)
        return longest
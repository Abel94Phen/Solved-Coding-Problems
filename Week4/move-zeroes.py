class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        read,write = 0,0
        while read < len(nums):
            if nums[read] != 0:
                nums[read], nums[write] = nums[write], nums[read]
                write += 1
            read += 1
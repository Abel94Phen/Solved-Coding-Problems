class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        right = nums[-1]
        splits = 0
        for i in range(len(nums) - 2, -1, -1):
            left = nums[i]
            if left > right:
                splits += ceil(left/right) - 1
                right = left // ceil(left/right)
            else:
                right = left
        return splits
            

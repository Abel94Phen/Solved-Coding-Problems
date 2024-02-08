class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        ##leftSum = 0
        for left in range(len(nums)):
            leftSum = nums[left - 1] if left > 0 else 0
            if leftSum == nums[-1] - nums[left]:
                return left
        return -1
        
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        result = [0 for _ in range(len(nums))]
        leftsum = 0
        rightsum = sum(nums)
        for i in range(len(nums)):
            rightsum -= nums[i]
            result[i] += (i * nums[i]) - leftsum
            result[i] += rightsum - (len(nums) - i - 1)*nums[i]
            leftsum += nums[i]
        return result
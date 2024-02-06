class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        score = 0
        nums = [sorted(num) for num in nums]

        for i in range(len(nums[0])):
            score += max([num[i] for num in nums])

        return score
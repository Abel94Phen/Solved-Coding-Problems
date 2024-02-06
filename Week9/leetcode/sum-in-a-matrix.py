class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        score = 0
        for i in range(len(nums[0])):
            max_val = 0
            for row in nums:
                x = max(row)
                max_val = max(max_val,x)
                row[row.index(x)] = -1
            score += max_val
        return score
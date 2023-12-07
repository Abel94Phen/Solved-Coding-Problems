class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1,-1]
        if target not in nums:
            return result
        result = [nums.index(target), nums.index(target)]
        for i in range(nums.index(target) + 1, len(nums)):
            if nums[i] == target:
                result[1] = i
        return result
            
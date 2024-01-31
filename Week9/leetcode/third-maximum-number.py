class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        third = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                third += 1
            if third == 3:
                return nums[i]
        return nums[0]
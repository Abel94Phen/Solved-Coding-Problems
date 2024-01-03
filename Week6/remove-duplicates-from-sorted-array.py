class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        place = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[place] = nums[i]
                place += 1
        return place
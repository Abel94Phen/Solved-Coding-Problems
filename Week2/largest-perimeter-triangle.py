class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        max_perimeter = 0
        for i in range(len(nums)-2):
            if nums[i] + nums[i+1] > nums[i+2] and nums[i+1] + nums[i] > nums[i+2] and nums[i+1] + nums[i+2] > nums[i]:
                max_perimeter = sum(nums[i:i+3])
                break
        return max_perimeter
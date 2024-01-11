class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = nums[0] + nums[1] + nums[len(nums) - 1]
        nums.sort()
        for i in range(len(nums)):
            
            j, k = i + 1, len(nums) - 1
            while j < k:
                Sum = nums[i] + nums[j] + nums[k]
                if  Sum > target:
                    k -= 1
                else:
                    j += 1
                
                if abs(Sum - target) < abs(result - target):
                    result = Sum

        return result            
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        i = len(nums) - 1
        prev = i - 1
        while prev >= 0:
            if prev + nums[prev] >= i:
                i = prev   
            prev -= 1
        
        if i == 0:    
            return True
        return False
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        """
        [1,5,10] 
        """
        patches = 0
        total = 0
        x = 1
        i = 0
        while total < n:
            if i < len(nums) and x >= nums[i]:
                total += nums[i]
                i += 1
            else:
                patches += 1
                total += x
            x = total + 1
            
        return patches
            
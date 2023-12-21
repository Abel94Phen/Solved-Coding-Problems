class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        nums_left = 0
        nums_right = sum(nums)
        
        
        result = []
        i = 0
        while i <= len(nums):
            if i == len(nums):
                if nums[-1] == 0:
                    nums_right = 0
                result.append(nums_right + nums_left)
                break
            result.append(nums_right + nums_left)
            if nums[i] == 0:
                nums_left += 1
            else:
                nums_right -= 1
            
            
                
            i += 1
        
        maximum = max(result)
        ans = list()
        for i in range(len(result)):
            if result[i] == maximum:
                ans.append(i)
        return ans
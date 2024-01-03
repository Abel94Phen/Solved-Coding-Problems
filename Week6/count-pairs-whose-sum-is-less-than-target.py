class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        i,j,count = 0,len(nums) - 1,0
        nums.sort()
        while i != j:
            if nums[i] + nums[j] < target:
                count += j - i
                i += 1
            else:
                j -= 1
              
        return count
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        "1,2,3,1,1,3,1,1"
        
        s = set(nums)
        result = 0
        for i in s:
            if nums.count(i) == 1:
                continue
            for j in range(nums.count(i), 0, -1):
                result += j - 1
        return result
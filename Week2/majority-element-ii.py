class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = set()
        L = set(nums)
        for i in L:
            if nums.count(i) > len(nums)//3:
                       result.add(i)
        return list(result)
        
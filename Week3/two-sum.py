class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        Comps = {}
        for i in range(len(nums)):
            if target - nums[i] in Comps:
                return [i, Comps[target - nums[i]]]
            Comps[nums[i]] = i
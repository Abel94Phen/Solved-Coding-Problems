class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number_sets = set()
        for i in nums:
            if i not in number_sets:
                number_sets.add(i)
            else:
                number_sets.remove(i)
        for i in number_sets:
            return i
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        deletions = 0
        for count in counts.values():
            if count == 1: 
                return -1
            deletions += ceil(count / 3)
        return deletions

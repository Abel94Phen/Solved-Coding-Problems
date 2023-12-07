class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives, negatives = [],[]
        for i in nums:
            if i > 0:
                positives.append(i)
            else:
                negatives.append(i)
        result = []
        for _ in range(len(nums)//2):
            result.append(positives[_])
            result.append(negatives[_])
        return result
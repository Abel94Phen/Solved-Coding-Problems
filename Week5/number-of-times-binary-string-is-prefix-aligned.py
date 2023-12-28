class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        aligned_at = 0
        for i,index in enumerate(flips):
            aligned_at = max(index,aligned_at)
            if i + 1 == aligned_at:
                count += 1
        return count
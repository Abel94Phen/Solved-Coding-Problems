class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = set()
        for i in ranges:
            covered.update(list(range(i[0], i[1] + 1)))
        for i in range(left, right+1):
            if i not in covered:
                return False
        return True
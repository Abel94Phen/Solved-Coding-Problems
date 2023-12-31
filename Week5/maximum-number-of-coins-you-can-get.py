class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        last = len(piles) - 2
        hashset = set()
        mysum = 0
        i = 0
        while i < len(piles) and last > 0:
            if last in hashset:
                break
            mysum += piles[last]
            last -= 2
            hashset.add(i)
            if i == 0:
                i += 2
            elif i % 2:
                i += 3
            elif not i % 2:
                i -= 1
        return mysum

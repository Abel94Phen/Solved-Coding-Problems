class Solution:
    def countOdds(self, low: int, high: int) -> int:
        length = (high - low + 1) // 2
        if not (high - low + 1)%2:
            return length
        elif (high - low + 1) % 2 and low%2:
            return length + 1
        else:
            return length


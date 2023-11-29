class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        num = n
        while n % 2:
            n += num
        return n
class Solution:
    def pivotInteger(self, n: int) -> int:
        total = (n + 1)*(n)//2
        prefix_sum = 0
        for i in range(1, n + 1):
            prefix_sum += i
            if prefix_sum == total:
                return i
            total -= i
        return -1

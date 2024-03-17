class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, 2**31 - 1
        while left < right - 1:
            mid = (left + right) // 2
            if mid*mid <= x:
                left = mid
            else:
                right = mid 
        return left
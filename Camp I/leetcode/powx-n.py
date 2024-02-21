class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(x, n):
            n = abs(n)
            if n == 0: return 1
            if n == 1: return x
            myInt = helper(x, n // 2)
            myInt = myInt * myInt
            if n % 2 : return x * myInt
            return myInt
        if n < 0: return 1 / helper(x, n)
        return helper(x, n)
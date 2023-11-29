class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        1  3  9  27  81  
        """
        for i in range(15,-1,-1):
            if 3 ** i <= n:
                n -= 3 ** i
            if n == 0:
                return True
        return False
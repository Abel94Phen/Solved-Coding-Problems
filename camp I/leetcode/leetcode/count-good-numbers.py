class Solution:
    def countGoodNumbers(self, n: int) -> int:
        ## simple answer with out recursion
        MOD = 10 ** 9 + 7
        count = 1
        count *= pow(4, n//2, MOD)
        count *= pow(5, (n + 1)//2, MOD)
        count %= MOD
        return count 

        
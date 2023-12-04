class Solution:
    def largestGoodInteger(self, num: str) -> str:
        decimals = "0123456789"
        i = 9
        while i > -1:
            if decimals[i]*3 in num:
                return decimals[i]*3
            i -= 1
        return ""
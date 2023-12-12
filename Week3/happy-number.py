class Solution:
    def isHappy(self, n: int) -> bool:
        nums = []
        while n not in nums:
            nums.append(n)
            var = 0
            while n > 0:
                var += (n%10)**2
                n //= 10
            n = var
            if n == 1: return True
        return False
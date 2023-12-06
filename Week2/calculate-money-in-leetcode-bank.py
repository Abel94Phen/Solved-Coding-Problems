class Solution:
    def totalMoney(self, n: int) -> int:
        money_in_bank = 0
        savings = [1,2,3,4,5,6,7]
        for i in range(n):
            money_in_bank += savings[i%7]
            savings[i%7] += 1
        return money_in_bank
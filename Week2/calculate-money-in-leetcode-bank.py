class Solution:
    def totalMoney(self, n: int) -> int:
        full_weeks = n // 7
        remaining_days = n % 7 

        sum_full_weeks = 28 * full_weeks + 7 * (full_weeks - 1) * full_weeks // 2
        sum_remaining_days = (full_weeks + full_weeks +2 + remaining_days - 1) * remaining_days // 2

        return sum_full_weeks + sum_remaining_days
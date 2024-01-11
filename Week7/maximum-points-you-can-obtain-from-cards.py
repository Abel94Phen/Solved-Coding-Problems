class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        i, j = 0, len(cardPoints) - 1
        left_win = 0
        right_win = k
        left_sum = 0
        right_sum = sum(cardPoints[len(cardPoints)-right_win:])
        max_sum = left_sum + right_sum
        while right_win > 0:
            right_sum -= cardPoints[len(cardPoints)-right_win]
            left_sum += cardPoints[left_win]
            right_win -= 1
            left_win += 1
            max_sum = max(max_sum, left_sum + right_sum)
        return max_sum

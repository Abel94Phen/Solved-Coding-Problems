class Solution:
    def maxScore(self, s: str) -> int:
        left_score = 0
        right_score = s.count('1')
        score = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                left_score += 1
            else:
                right_score -= 1

            score = max(score, left_score + right_score)
        return score
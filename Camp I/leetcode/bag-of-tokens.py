class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens) - 1
        max_score = 0
        score = 0
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
            elif score >= 1:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
            max_score = max(max_score, score)
        
        return max_score
        

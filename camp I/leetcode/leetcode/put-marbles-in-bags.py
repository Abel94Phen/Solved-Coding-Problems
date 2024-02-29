class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        scores = []
        for i in range(len(weights) - 1):
            scores.append(weights[i] + weights[i + 1])
        scores.sort()
        min_score = max_score = weights[0] + weights[-1]
        for i in range(k - 1):
            min_score += scores[i]
            max_score += scores[len(scores) - i - 1]
        return max_score - min_score
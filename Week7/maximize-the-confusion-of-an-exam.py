class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        occurrences = {'T':0, 'F':0}
        max_length = 0
        left = 0
        for right in range(len(answerKey)):
            occurrences[answerKey[right]] += 1
            while min(occurrences['T'], occurrences['F']) > k:
                occurrences[answerKey[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
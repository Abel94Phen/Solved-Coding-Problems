class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = defaultdict()
        max_frequency = 0
        result = 0
        left = 0
        for right in range(len(s)):
            frequencies[s[right]] = frequencies.get(s[right], 0) + 1
            max_frequency = max(max_frequency, frequencies[s[right]])
            
            while (right - left + 1) - max_frequency > k:
                frequencies[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        return result
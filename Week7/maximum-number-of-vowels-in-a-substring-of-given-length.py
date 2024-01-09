class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        i, max_count, count = 0, 0, 0
        for j in range(len(s)):
            count += 1 if s[j] in vowels else 0
            if j - i + 1 > k:
                if s[i] in vowels:
                    count -= 1
                i += 1
            max_count = max(max_count,count)
        return max_count
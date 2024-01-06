class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        max_length = 0
        i = 0
        for j in range(len(s)):
            while s[j] in chars:
                chars.remove(s[i])
                i += 1
            chars.add(s[j])
            max_length = max(max_length, j - i + 1)
        return max_length
            
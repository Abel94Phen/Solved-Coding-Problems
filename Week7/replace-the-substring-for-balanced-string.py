class Solution:
    def balancedString(self, s: str) -> int:
        hashmap = {"Q":0, "W":0, "E":0, "R":0}
        for _ in s:
            hashmap[_] += 1
        occurrence = len(s) // 4
        min_len = len(s)
        left = 0
        for right in range(len(s)):
            hashmap[s[right]] -= 1
            while (
                left < len(s)
                and hashmap["Q"] <= occurrence
                and hashmap["W"] <= occurrence
                and hashmap["E"] <= occurrence
                and hashmap["R"] <= occurrence
            ):
                min_len = min(min_len, right - left + 1)
                hashmap[s[left]] += 1
                left += 1
        return min_len

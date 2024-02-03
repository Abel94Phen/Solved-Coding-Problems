class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        if len(set(list(s))) != 3:
            return 0
        sub_strings = 0
        hashmap = dict()
        left = 0
        for right in range(len(s)):
            if s[right] in hashmap:
                hashmap[s[right]] += 1
            else:
                hashmap[s[right]] = 1
            while len(hashmap) == 3:
                sub_strings += len(s) - right
                hashmap[s[left]] -= 1
                if hashmap[s[left]] == 0:
                    del hashmap[s[left]]
                left += 1
        return sub_strings
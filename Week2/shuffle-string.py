class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        mapping = dict()
        for i in range(len(s)):
            mapping[indices[i]] = s[i]
        mapping = sorted(mapping.items(), key=lambda x:x[0])
        result = ""
        for i in mapping:
            result += i[1]
        return result
        
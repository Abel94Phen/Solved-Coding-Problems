class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        string = list(s)
        for i in range(0, len(s), 2*k):
            string[i:i+k] = string[i:i+k][::-1]
        return ''.join(string)
class Solution:
    def romanToInt(self, s: str) -> int:
        basicDict = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and basicDict[s[i + 1]] > basicDict[s[i]]:
                result -= basicDict[s[i]]
            else:
                result += basicDict[s[i]]
        return result
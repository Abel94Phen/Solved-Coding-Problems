class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        last = len(s) - 1
        while i < last:
            temp = s[i]
            s[i] = s[last]
            s[last] = temp
            i += 1
            last -= 1
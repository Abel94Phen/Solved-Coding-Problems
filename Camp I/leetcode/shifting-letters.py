class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prefix_shift = [0 for _ in range(len(shifts))]
        for i in range(len(shifts)):
            prefix_shift[0] += shifts[i]
            if i != len(shifts) - 1:
                prefix_shift[i + 1] -= shifts[i]
        for i in range(1, len(shifts)):
            prefix_shift[i] += prefix_shift[i - 1]
        
        result = ""
        for i in range(len(s)):
            num_c = ord(s[i]) + prefix_shift[i]
            result += chr(97 + (num_c - 97)%26)
        
        return result
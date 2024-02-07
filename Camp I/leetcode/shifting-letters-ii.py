class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum = [0 for _ in range(len(s))]
        for shift in shifts:
            if shift[2] == 1:
                prefix_sum[shift[0]] += 1
                if shift[1] != len(s) - 1:
                    prefix_sum[shift[1] + 1] -= 1
            elif shift[2] == 0:
                prefix_sum[shift[0]] -= 1
                if shift[1] != len(s) - 1:
                    prefix_sum[shift[1] + 1] += 1
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i - 1]
        
        result = ""
        for i in range(len(s)):
            num_c = ord(s[i]) + prefix_sum[i]
            result += chr(97 + (num_c - 97)%26)
            
        return result
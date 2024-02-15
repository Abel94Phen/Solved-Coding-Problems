class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = 0
        ones = False
        for count in counts:
            if counts[count]%2:
                length += (counts[count] - 1)
                counts[count] = 1
                ones = True

            else:
                length += counts[count]

        if ones:
            length += 1        

        return length
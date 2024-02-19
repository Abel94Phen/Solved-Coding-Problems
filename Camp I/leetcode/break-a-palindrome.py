class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        elif palindrome.count('a') == len(palindrome) or palindrome.count('a') == len(palindrome) - 1:
            return palindrome[:-1] + 'b'
        else:
            palindrome = list(palindrome)
            i = 0
            while palindrome[i] == 'a':
                i += 1
            palindrome[i] = 'a'
            return ''.join(palindrome)
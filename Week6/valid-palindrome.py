class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(letter for letter in s if letter.isalnum()).lower()
        first, last = 0, len(s) - 1
        while first < last:
            if s[first] != s[last]:
                return False
            first += 1
            last -= 1
        return True
        
            
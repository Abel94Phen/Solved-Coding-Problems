class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        asterisks = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == '*':
                asterisks.append(i)
            else:
                if stack:
                    stack.pop()
                elif asterisks:
                    asterisks.pop()
                else:
                    return False
            
        while stack:
            if asterisks and stack[-1] < asterisks[-1]:
                stack.pop()
                asterisks.pop()
            else:
                return False
        return True

        # TC: O(n)
        # SC: O(n)

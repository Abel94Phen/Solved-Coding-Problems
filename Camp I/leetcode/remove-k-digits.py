class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in range(len(num)):
            if not stack:
                stack.append(int(num[i]))
            else:
                while k and stack and stack[-1] > int(num[i]):
                    stack.pop()
                    k -= 1
                stack.append(int(num[i]))
        
        while k:
            stack.pop()
            k -= 1

        start = 0
        while start < len(stack) and stack[start] == 0:
            start += 1
        
        if start == len(stack):
            return "0"

        result = ""
        while start < len(stack):
            result += str(stack[start])
            start += 1
        return result

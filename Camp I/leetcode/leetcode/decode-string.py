class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1].isalpha() and char.isalpha():
                stack[-1] += char
            elif char.isalpha():
                stack.append(char)
            elif stack and stack[-1].isnumeric() and char.isnumeric():
                stack[-1] += char
            elif char.isnumeric():
                stack.append(char)
            elif char == '[':
                stack.append(char)
            else:
                string = stack.pop()
                stack.pop()
                multiplier = int(stack.pop())
                if stack and stack[-1] != '[':
                    stack[-1] += multiplier * string
                else:
                    stack.append(multiplier * string)
            
            print(stack)
        return stack[0]
                
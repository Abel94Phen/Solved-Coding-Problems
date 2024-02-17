class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if not token.lstrip('-+').isdigit():
                x = stack.pop()
                y = stack.pop()
                result = 0
                if token == '+':
                    result = x + y
                elif token == '-':
                    result = y - x
                elif token == '*':
                    result = x * y
                else:
                    result = int(y / x)
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack[0]
        
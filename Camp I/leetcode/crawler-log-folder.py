class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        length = 0
        for log in logs:
            if stack and log == '../':
                stack.pop()
                length -= 1
            elif log == '../' or log == './':
                continue
            
            else:
                stack.append(log)
                length += 1
        return length
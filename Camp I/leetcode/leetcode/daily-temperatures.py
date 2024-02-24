class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)):
            if not stack:
                stack.append((i, temperatures[i]))
            else:
                if stack[-1][1] >= temperatures[i]:
                    stack.append((i, temperatures[i]))
                else:
                    while stack and stack[-1][1] < temperatures[i]:
                        result[stack[-1][0]] = i - stack[-1][0]
                        stack.pop()
                    stack.append((i, temperatures[i]))
        
        return result



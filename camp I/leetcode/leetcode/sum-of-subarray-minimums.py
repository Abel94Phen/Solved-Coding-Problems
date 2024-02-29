class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = (10 ** 9) + 7
        result = 0
        stack = []
        for i, num in enumerate(arr):
            while stack and num < stack[-1][1]:
                index, val = stack.pop()
                left = index - stack[-1][0] if stack else index + 1
                right = i - index
                result = (result + val * left * right) % MOD
            stack.append((i, num))

        for k in range(len(stack)):
            index, val = stack[k]
            left = index - stack[k - 1][0] if k > 0 else index + 1
            right = len(arr) - index
            result = (result + val * left * right) % MOD
        
        return result
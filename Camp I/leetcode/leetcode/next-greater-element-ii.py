class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        L = len(nums)
        result = [-1 for _ in range(L)]
        stack = []
        for i in range(2 * L):
            if not stack:
                stack.append((nums[i%L], i%L))
            else:
                while stack and stack[-1][0] < nums[i%L]:
                    if result[stack[-1][1]] == -1:
                        result[stack[-1][1]] = nums[i%L]
                    stack.pop()
                stack.append((nums[i%L], i%L))
        return result
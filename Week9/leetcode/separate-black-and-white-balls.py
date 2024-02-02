class Solution:
    def minimumSteps(self, s: str) -> int:
        if len(s) == 1: return 0
        left, right = 0, 1
        balls = list(s)
        swaps = 0
        while right < len(s):
            if balls[left] == '1' and balls[right] == '0':
                balls[left], balls[right] = balls[right], balls[left]
                swaps += right - left
                left += 1
            elif balls[left] == '0':
                left += 1
            right += 1
           
        return swaps
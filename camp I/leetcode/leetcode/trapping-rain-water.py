class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0 for _ in range(len(height))]
        max_right = [0 for _ in range(len(height))]
        
        max_height = height[0]
        for i in range(len(height)):
            max_left[i] = max_height
            max_height = max(height[i], max_height)

        max_height = height[len(height) - 1]
        for i in range(len(height) - 1, -1, -1):
            max_right[i] = max_height
            max_height = max(height[i], max_height)
        
        trapped = 0

        for i in range(len(height)):
            volume = min(max_right[i], max_left[i]) - height[i]
            trapped += volume if volume > 0 else 0
            

        
        return trapped
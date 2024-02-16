class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        points.sort(key = lambda x : x[1])
        
        left, right = 0, 1
        arrows = 0
        while left < len(points):
            while right < len(points) and points[left][1] >= points[right][0]:
                right += 1
            left = right
            right += 1

            arrows += 1
        
        return arrows
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda point:point[0])
        area = 0
        for i in range(len(points)-1):
            area = max(area, points[i+1][0] - points[i][0])
        return area
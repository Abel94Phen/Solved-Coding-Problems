class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        path = [0 for _ in range(1001)]
        for trip in trips:
            path[trip[1]] += trip[0]
            path[trip[2]] -= trip[0]
        for i in range(1, 1001):
            path[i] += path[i - 1]
        
        if max(path) <= capacity:
            return True
        else:
            return False
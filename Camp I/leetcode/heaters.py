class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def close_from_left(position):
            if position < heaters[0]:
                return None
            left, right = -1, len(heaters)
            while left < right - 1:
                mid = (left + right) //2
                if heaters[mid] <= position:
                    left = mid
                else:
                    right = mid
            return heaters[left]

        def close_from_right(position):
            if position > heaters[-1]:
                return None
            left, right = -1, len(heaters)
            while left < right - 1:
                mid = (left + right) //2
                if heaters[mid] < position:
                    left = mid
                else:
                    right = mid
            return heaters[right]
        
        houses.sort()
        heaters.sort()
        closest = []
        for house in houses:
            closest.append([house, close_from_left(house)])
        
        for i in range(len(closest)):
            alternate = close_from_right(closest[i][0])
            if closest[i][1] == None:
                closest[i][1] = alternate
            elif alternate:
                if abs(closest[i][0] - alternate) < abs(closest[i][0] - closest[i][1]):
                    closest[i][1] = alternate        
        
        radius = 0
        for pair in closest:
            radius = max(radius, abs(pair[0] - pair[1]))
        return radius

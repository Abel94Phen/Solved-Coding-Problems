class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        clockwise = 0
        anticlockwise = 0
        i = start
        while (i%len(distance)) != destination:
            clockwise += distance[i%len(distance)]
            i += 1
        i = start
        while (i%len(distance)) != destination:
            i -= 1
            anticlockwise += distance[(i)%len(distance)]
            
        print(clockwise,anticlockwise)
        return min(clockwise,anticlockwise)
            
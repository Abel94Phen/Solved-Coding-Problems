class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle =  list(range(1, n+1))
        starting = circle[0]
        i = -1
        while len(circle) > 1:
            i += k
            starting = circle[(i+1) % len(circle)]
            circle.pop(i % len(circle))
            i = circle.index(starting) - 1
        
        return circle[0]
            
            
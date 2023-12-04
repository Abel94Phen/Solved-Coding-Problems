class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        i = -1
        fill = capacity
        """
        [1,1,1,4,2,3]
        
        4
        """
        while i < len(plants)-1:
            if capacity >= plants[i+1]:
                i += 1
                steps += 1
                capacity -= plants[i]
            else:
                capacity = fill
                steps += 2*(i + 1)
                
            
        return steps
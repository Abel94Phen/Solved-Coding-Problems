class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while target > 1:
            if target % 2:
                moves += 1
                target -= 1
            
            if maxDoubles > 0:
                target //= 2
                maxDoubles -= 1
                moves += 1
            
            else:
                moves += target - 1
                target = 1

        
        
        return moves


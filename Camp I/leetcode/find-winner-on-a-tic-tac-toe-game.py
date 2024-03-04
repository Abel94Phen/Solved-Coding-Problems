class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        """
        1 2 3
        4 5 6
        7 8 9
        """
        grid = [[None for _ in range(3)] for _ in range(3)]
        turn = True
        for move in moves:
            if turn:
                grid[move[0]][move[1]] = "X"
            else:
                grid[move[0]][move[1]] = "C"
            turn = not turn

        for row in grid:
            if row.count('X') == 3:
                return 'A'
            elif row.count('C') == 3:
                return 'B'

        for i in range(3):
            if grid[0][i] == grid[1][i] == grid[2][i] == 'X':
                return 'A'
            elif grid[0][i] == grid[1][i] == grid[2][i] == 'C':
                return 'B'
        
        if grid[0][0] == grid[1][1] == grid[2][2] == 'X' or grid[0][2] == grid[1][1] == grid[2][0] == 'X':
            return 'A'
        elif grid[0][0] == grid[1][1] == grid[2][2] == 'C' or grid[0][2] == grid[1][1] == grid[2][0] == 'C':
            return 'B'
        
        
        
        if len(moves) == 9:
            return "Draw"
        return "Pending"

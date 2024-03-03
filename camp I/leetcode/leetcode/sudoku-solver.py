class Solution:
    def __init__(self):
        self.solved = False
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r//3,c//3)].add(board[r][c])
        
        def backtrack(i, j):
            if i == 9:
                return True
            
            if j == 9:
                return backtrack(i+1,0)
            
            
            if board[i][j] == ".":
                for num in range(1,10):
                    if str(num) not in rows[i] and str(num) not in cols[j] and str(num) not in boxes[(i//3,j//3)]:
                        board[i][j] = str(num)
                        rows[i].add(board[i][j])
                        cols[j].add(board[i][j])
                        boxes[(i//3,j//3)].add(board[i][j])
                        
                        
                        if backtrack(i,j+1):
                            return True
                        
                        else:
                            rows[i].remove(board[i][j])
                            cols[j].remove(board[i][j])
                            boxes[(i//3,j//3)].remove(board[i][j])
                            board[i][j] = "."
                return False
            else:
                return backtrack(i,j+1)
        
        backtrack(0, 0)
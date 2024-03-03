class Solution:
    def totalNQueens(self, n: int) -> int:
        files = set()
        primary = set()
        secondary = set()

        chessboard = [["." for _ in range(n)] for _ in range(n)]
        self.positions = 0

        def backtrack(row):
            if row == n:
                self.positions += 1
                return
            
            for col in range(n):
                if col in files or (row - col) in primary or (row + col) in secondary:
                    continue

                files.add(col)
                primary.add(row - col)
                secondary.add(row + col)
                chessboard[row][col] = "Q"

                backtrack(row + 1)

                files.remove(col)
                primary.remove(row - col)
                secondary.remove(row + col)
                chessboard[row][col] = "."

        backtrack(0)
        return self.positions
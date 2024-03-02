class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        seen = set()

        def backtrack(R, C, index):
            if index == len(word):
                return True

            if R < 0 or C < 0 or R >= row or C >= col or word[index] != board[R][C] or (R, C) in seen:
                return False

            seen.add((R, C))
            result = backtrack(R + 1, C, index + 1) or backtrack(R, C + 1, index + 1) or backtrack(R - 1, C, index + 1) or backtrack(R, C - 1, index + 1)
            seen.remove((R, C))
            return result

        for i in range(row):
            for j in range(col):
                if backtrack(i, j, 0):
                    return True
        return False
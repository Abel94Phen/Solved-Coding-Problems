class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = [max(row) for row in grid]
        col_max = []
        for i in range(len(grid)):
            column = []
            for row in grid:
                column.append(row[i])
            col_max.append(max(column))
        max_increase = 0
        for row in range(len(grid)):
            for col in range(len(grid)):
                max_increase += min(row_max[row], col_max[col]) - grid[row][col]
        return max_increase

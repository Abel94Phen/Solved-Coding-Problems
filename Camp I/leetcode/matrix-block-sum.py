class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        prefix_matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                prefix_matrix[row][col] += prefix_matrix[row - 1][col]
                prefix_matrix[row][col] += prefix_matrix[row][col - 1] 
                prefix_matrix[row][col] -= prefix_matrix[row - 1][col - 1]
                prefix_matrix[row][col] += mat[row - 1][col - 1]
        
        # print(prefix_matrix)

        result = [[0 for _ in range(n)] for _ in range(m)]
        for row in range(m):
            for col in range(n):
                r1 = 0 if row - k < 0 else row - k
                c1 = 0 if col - k < 0 else col - k
                r2 = m - 1 if row + k >= m else row + k
                c2 = n - 1 if col + k >= n else col + k

                
                result[row][col] += prefix_matrix[r2 + 1][c2 + 1]
                result[row][col] -= prefix_matrix[r1][c2 + 1]
                result[row][col] -= prefix_matrix[r2 + 1][c1]
                result[row][col] += prefix_matrix[r1][c1]

        return result
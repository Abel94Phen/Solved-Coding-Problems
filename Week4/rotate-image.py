class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        intermediate = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                intermediate[j][i] = matrix[i][j]
                
        for row in intermediate:
            row.reverse()
            
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = intermediate[i][j]
                
        
        
        return matrix
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i, j = 0, 0
        sum = 0
        while i < len(mat) and j < len(mat):
            sum += mat[i][j]
            i += 1
            j += 1
        
        
        i -= 1
        j = 0

        while i > -1:
            sum += mat[i][j]
            i -= 1
            j += 1
        
        return sum - mat[len(mat)//2][len(mat)//2] if len(mat)%2 else sum


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        prefix_matrix = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        submatrices = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                prefix_matrix[row + 1][col + 1] += prefix_matrix[row][col + 1]
                prefix_matrix[row + 1][col + 1] += prefix_matrix[row + 1][col]
                prefix_matrix[row + 1][col + 1] -= prefix_matrix[row][col]
                prefix_matrix[row + 1][col + 1] += matrix[row][col]
            
        
        for r1 in range(1, len(prefix_matrix)):
            for r2 in range(r1, len(prefix_matrix)):
                hashmap = {0:1}
                for col in range(1, len(prefix_matrix[0])):
                    curr_sum = prefix_matrix[r2][col] - prefix_matrix[r1 - 1][col]
                    needed = curr_sum - target
                    submatrices += hashmap.get(needed, 0)
                    hashmap[curr_sum] = hashmap.get(curr_sum, 0) + 1

        return submatrices
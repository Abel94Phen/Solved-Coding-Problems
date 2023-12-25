class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals = collections.defaultdict(list)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diagonals[i+j].append(mat[i][j])

        result = []

        for diagonal in diagonals.keys():
            if not diagonal%2:
                result += diagonals[diagonal][::-1]
            else:
                result += diagonals[diagonal]
        return result
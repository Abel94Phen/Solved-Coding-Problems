class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(rowIndex + 1):
            x = factorial(rowIndex) / (factorial(rowIndex - i) * factorial(i))
            result.append(int(x))
        return result
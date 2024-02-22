class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prev = self.getRow(rowIndex - 1)
        ans = []
        for i in range(len(prev) + 1):
            if i == 0 or i == len(prev):
                ans.append(1)
            else:
                ans.append(prev[i] + prev[i - 1])
        return ans
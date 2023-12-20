class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        columns_to_be_deleted = 0
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if strs[j][i] < strs[j-1][i]:
                    columns_to_be_deleted += 1
                    break
        return columns_to_be_deleted
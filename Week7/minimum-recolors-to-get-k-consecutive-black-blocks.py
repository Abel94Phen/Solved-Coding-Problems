class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        max_Length = 0
        for i in range(len(blocks) - k + 1):
            max_Length = max(max_Length, blocks[i : i + k].count('B'))
        return k - max_Length
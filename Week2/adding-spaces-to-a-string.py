class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        spaces = set(spaces)
        for i,c in enumerate(s):
            if i in spaces:
                result.append(' ')
            result.append(c)
        return ''.join(result)
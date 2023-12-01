class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for j in range(len(words)-1):
            x = min(len(words[j]), len(words[j+1]))
            for i in range(x):
                if order.index(words[j][i]) < order.index(words[j+1][i]):
                    break
                elif order.index(words[j][i]) > order.index(words[j+1][i]) or (len(words[j]) > len(words[j+1]) and i == x-1):
                    return False
        return True

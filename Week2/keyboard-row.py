class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        possible = []
        for word in words:
            for i in range(3):
                if set(word.lower()).issubset(keyboard[i]):
                    possible.append(word)
        return possible
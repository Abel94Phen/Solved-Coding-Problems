class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        score = 0
        word = []
        for char in s:
            if char == ')' and score > 0:
                word.append(char)
                score -= 1
            if char != ')':
                word.append(char)
                if char == '(':
                    score += 1

        for i in range(len(word) - 1, -1, -1):
            if score > 0 and word[i] == '(':
                word[i] = None
                score -= 1

        result = ""
        for char in word:
            if char:
                result += char
        return result

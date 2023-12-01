class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_word = ""
        i = 0
        while i < min(len(word1),len(word2)):
            merged_word += word1[i] + word2[i]
            i += 1
        merged_word += word1[i:] + word2[i:] 
        return merged_word
        
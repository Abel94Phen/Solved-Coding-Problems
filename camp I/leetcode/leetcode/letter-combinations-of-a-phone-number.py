class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}

        result = []

        
        def backtrack(index, string):
            if len(string) == len(digits):
                result.append(string)
                return

            for char in hashmap[digits[index]]:
                backtrack(index + 1, string + char)

        if digits:
            backtrack(0, "")
            return result
        return []

        
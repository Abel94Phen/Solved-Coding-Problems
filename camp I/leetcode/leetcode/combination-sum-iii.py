class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        combination = []
        def backtrack(index, length, target):
            if len(combination) == length and target == 0:
                result.append(combination.copy())
                return

            if target == 0:
                return

                
            for i in range(index, 10):
                
                combination.append(i)
                backtrack(i + 1, length, target - i)
                combination.pop()
                
                
            
        backtrack(1, k, n)
        return result
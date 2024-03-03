class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        combination = []
        def backtrack(index, total):
            if total == target:
                result.append(combination.copy())
                return

            if total > target or index == len(candidates):
                return
                
            combination.append(candidates[index])
            backtrack(index, total + candidates[index])
            combination.pop()
            backtrack(index + 1, total)

        backtrack(0, 0)
        return result

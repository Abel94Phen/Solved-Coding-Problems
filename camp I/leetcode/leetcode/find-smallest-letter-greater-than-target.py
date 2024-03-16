class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = -1, len(letters)
        while left < right - 1:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid
            else:
                right = mid
        
        if left == len(letters) - 1:
            return letters[0]
        return letters[left + 1]
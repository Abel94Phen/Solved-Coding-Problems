class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        """
        x ---- if x can become num then x is achievable
        
        t ---- number of times increment or decrement can happen
        
        num ---- input
        
        """
        return num + (2*t)
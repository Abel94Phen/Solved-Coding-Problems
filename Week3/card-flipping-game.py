class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        card_numbers = set(fronts + backs)

        for f,b in zip(fronts, backs):
            if f == b:
                card_numbers.discard(f) # need discard instead of remove. ex. [1,1], [1,1]
        
        return min(card_numbers, default = 0)
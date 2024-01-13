class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hashmap = {}
        min_length = float('inf')
        for i in range(len(cards)):
            if cards[i] in hashmap:
                min_length = min(min_length, i - hashmap[cards[i]] + 1)    
            hashmap[cards[i]] = i

        if min_length == float('inf'):
            return -1
        
        return min_length
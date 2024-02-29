class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        result = [0 for _ in range(len(deck))] 
        queue = deque(range(len(deck)))
        for card in deck:
            result[queue.popleft()] = card
            if queue:
                queue.append(queue.popleft())
            
        return result
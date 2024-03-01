class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        radiant, dire = deque(), deque()
        
        for index, char in enumerate(senate):
            if char == 'R':
                radiant.append(index)
            else:
                dire.append(index)
        
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                radiant.append(r + len(senate))
            else:
                dire.append(d + len(senate))
        
        return 'Dire' if dire else 'Radiant'
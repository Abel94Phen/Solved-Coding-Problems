class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hashtable = dict(Counter(answers))
        rabbits = 0
        for answer,frequency in hashtable.items():
            rabbits += (answer + 1) * ceil(frequency/(answer + 1))
        return rabbits
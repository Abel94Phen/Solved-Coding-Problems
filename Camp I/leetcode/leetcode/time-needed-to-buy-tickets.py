class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time_taken = 0
        for i in range(tickets[k]):
            for j in range(len(tickets)):
                if tickets[j] > 0:
                    tickets[j] -= 1
                    time_taken += 1
                
                if tickets[k] == 0:
                    return time_taken
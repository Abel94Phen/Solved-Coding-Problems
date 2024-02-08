class Solution:
    def bestClosingTime(self, customers: str) -> int:
        leftPenalty = 0
        rightPenalty = customers.count('Y')
        minPenalty = (leftPenalty + rightPenalty, 0)

        for i in range(len(customers)):
            if customers[i] == 'N':
                leftPenalty += 1
            if customers[i] == 'Y':
                rightPenalty -= 1
            
            if leftPenalty + rightPenalty < minPenalty[0]:
                minPenalty = (leftPenalty + rightPenalty, i + 1)
        
        return minPenalty[1]

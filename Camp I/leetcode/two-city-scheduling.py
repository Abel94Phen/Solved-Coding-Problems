class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x : x[0] - x[1])
        length = len(costs)
        result = 0
        for i in range(length):
            if i < length/2:
                result += costs[i][0]
            else:
                result += costs[i][1]
        return result
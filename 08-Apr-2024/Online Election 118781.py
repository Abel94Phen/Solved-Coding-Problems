# Problem: Online Election - https://leetcode.com/problems/online-election/

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.data = []
        hashmap = {}
        leader = 0
        for i in range(len(times)):
            hashmap[persons[i]] = hashmap.get(persons[i], 0) + 1
            if hashmap[persons[i]] >= hashmap.get(leader, 0):
                leader = persons[i]
            self.data.append((times[i], leader))

    def q(self, t: int) -> int:
        left, right = -1, len(self.data)
        while left < right - 1:
            mid = (left + right) // 2
            if self.data[mid][0] <= t:
                left = mid
            else:
                right = mid
        return self.data[left][1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
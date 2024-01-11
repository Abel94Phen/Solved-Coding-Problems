class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters = dict(Counter(s1))
        temp = dict(Counter(s2[:len(s1)]))
        if letters == temp:
            return True
        for i in range(len(s2) - len(s1)):
            temp[s2[i]] -= 1
            if temp[s2[i]] == 0:
                del temp[s2[i]]

            temp[s2[i + len(s1)]] = temp.get(s2[i + len(s1)], 0) + 1
            if letters == temp:
                return True            
        return False
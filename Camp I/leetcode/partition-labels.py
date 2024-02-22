class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partitions = []
        hashtable = {}
        for i in range(len(s)):
            hashtable[s[i]] = i
        
        first = 0
        while first < len(s):
            last = hashtable[s[first]]
            first += 1
            while first < last:
                if hashtable[s[first]] > last:
                    last = hashtable[s[first]]
                first += 1
            partitions.append(last)
            last += 1
            first = last
        
        for i in range(len(partitions)):
            partitions[i] += 1
        for i in range(len(partitions) - 1, 0, -1):
            partitions[i] -= partitions[i - 1]
        return partitions
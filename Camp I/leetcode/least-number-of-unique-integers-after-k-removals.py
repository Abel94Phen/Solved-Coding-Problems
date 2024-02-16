class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)
        frequencies = []
        for count in counts:
            frequencies.append(counts[count])
        frequencies.sort()
        i = 0
        while frequencies and frequencies[i] <= k:
            k -= frequencies[i]
            frequencies.pop(0)
        return len(frequencies)
        
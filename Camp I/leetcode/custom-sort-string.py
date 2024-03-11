class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashmap = {}
        for index, char in enumerate(order):
            hashmap[char] = index        
        return ''.join(sorted(s, key = lambda x : hashmap.get(x, float('inf'))))

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(list)
        for i in range(len(nums)):
            hashmap[nums[i]].append(i)
        
        result = [0 for _ in range(len(nums))]

        for val in dict(hashmap):
            rightSum = sum(hashmap[val])
            leftSum = 0
            for i in range(len(hashmap[val])):
                rightSum -= hashmap[val][i]
                result[hashmap[val][i]] += hashmap[val][i] * i - leftSum
                result[hashmap[val][i]] += rightSum - (hashmap[val][i] * (len(hashmap[val]) - i - 1))
                leftSum += hashmap[val][i]
        
        return result
                                                       
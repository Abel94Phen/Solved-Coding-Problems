class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        ## [1,3,6,10,15] == > original permutation
        ## [2,3,6,10,15] == > first permutation
        ## [3,8,12,14,15] == > second permutation
        length = len(nums)
        MOD = 10 ** 9 + 7
        index_prefix = [0 for _ in range(length)]
        for request in requests:
            index_prefix[request[0]] += 1
            if  request[1] != length - 1:
                index_prefix[request[1] + 1] -= 1
        
        for i in range(1, length):
            index_prefix[i] += index_prefix[i - 1]

        index_prefix.sort(reverse = True)
        nums.sort(reverse = True)

        result = 0
        for i in range(length):
            result += index_prefix[i] * nums[i]
        
        return result % MOD
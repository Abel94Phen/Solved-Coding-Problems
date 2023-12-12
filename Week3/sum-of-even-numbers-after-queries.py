class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums_sum = sum(num for num in nums if num%2 == 0)
        
        result = []
        
        for query in queries:
            before_query = nums[query[1]]
            nums[query[1]] += query[0]
            after_query = nums[query[1]]
            
            if before_query%2 != 0 and after_query%2 == 0:
                nums_sum += after_query
            elif before_query%2 == 0 and after_query%2 != 0:
                nums_sum -= before_query
            elif before_query%2 == 0 and after_query%2 == 0:
                nums_sum += query[0]
            
            
            result.append(nums_sum)
        return result
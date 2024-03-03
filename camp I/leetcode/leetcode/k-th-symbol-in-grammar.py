class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        ## Who Knew this turned out to be a binary search problem 
        root = 0
        left, right = 1, 2 ** (n - 1)

        while left < right:
            mid = (left + right) // 2
            if k <= mid:
                right = mid
            
            else:
                left = mid + 1
                root = 0 if root else 1
            
        return root


        
        return queue[k - 1]

            


            
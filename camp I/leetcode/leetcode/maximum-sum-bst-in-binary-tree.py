# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_sum = 0

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
        def makeSum(root):
            while root:
                left_max, left_min, leftIsValid, left_sum = makeSum(root.left)
                right_max, right_min, rightIsValid, right_sum = makeSum(root.right)
                
                while leftIsValid and rightIsValid and left_max < root.val < right_min:
                        curr_sum = root.val + left_sum + right_sum
                        self.max_sum = max(self.max_sum, curr_sum)
                        return (max(root.val,right_max), min(left_min,root.val),True,curr_sum)
                
                return (float("-inf"), float("inf"), False, 0)
            
            return (float("-inf"),float("inf"),True, 0)
        
        makeSum(root)
        return self.max_sum
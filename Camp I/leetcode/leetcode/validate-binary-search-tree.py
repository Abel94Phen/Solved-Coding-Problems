# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(root, left_bound, right_bound):
            if not root:
                return True
            
            if left_bound >= root.val or right_bound <= root.val:
                return False

            return validate(root.left, left_bound, root.val) and validate(root.right, root.val, right_bound)

        return validate(root, float('-inf'), float('inf'))
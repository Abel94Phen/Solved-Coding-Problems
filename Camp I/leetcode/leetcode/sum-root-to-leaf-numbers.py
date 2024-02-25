# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total_leaf_sum = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def root_to_leaf_sum(root, currentSum = 0):
            if not root:
                return
            
            root.val = currentSum * 10 + root.val
            root_to_leaf_sum(root.left, root.val)
            root_to_leaf_sum(root.right, root.val)

        def leaf_sum(root):
            if not root:
                return
            
            if not root.left and not root.right:
                self.total_leaf_sum += root.val
            
            leaf_sum(root.left)
            leaf_sum(root.right)
            
        root_to_leaf_sum(root)
        leaf_sum(root)

        return self.total_leaf_sum
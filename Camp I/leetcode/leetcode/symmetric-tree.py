# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.left_tree = []
        self.right_tree = []
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def validate(left_tree, right_tree):
            if not left_tree and not right_tree:
                return True
            
            elif not left_tree or not right_tree:
                return False

            else:
                return left_tree.val == right_tree.val and validate(left_tree.left, right_tree.right) and validate(left_tree.right, right_tree.left)

        return validate(root.left, root.right)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.values = []

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def traverse_inorder(root):
            if root:
                traverse_inorder(root.left)
                self.values.append(root.val)
                traverse_inorder(root.right)
        traverse_inorder(root)
        return self.values[k - 1]
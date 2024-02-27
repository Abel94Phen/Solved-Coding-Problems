# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.values = []

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def traverse_inorder(root):
            if root:
                traverse_inorder(root.left)
                self.values.append(root.val)
                traverse_inorder(root.right)
        traverse_inorder(root)
        
        for i in range(len(self.values) - 1):
            if self.values[i] == self.values[i + 1]:
                return False
        return sorted(self.values) == self.values
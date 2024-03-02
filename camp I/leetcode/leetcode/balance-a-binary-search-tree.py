# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        values = []
        def traverse(root):
            if not root:
                return

            traverse(root.left)
            values.append(root.val)
            traverse(root.right)

        def makeBST(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            left = makeBST(left, mid - 1)
            right = makeBST(mid + 1, right)
            return TreeNode(values[mid], left, right)

        traverse(root)
        return makeBST(0, len(values) - 1)
        
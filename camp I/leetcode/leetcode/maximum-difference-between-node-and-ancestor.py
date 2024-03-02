# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_diff = 0

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def helper(root):
            if not root:
                return [float('inf'), float('-inf')]

            if not root.left and not root.right:
                return [root.val, root.val]

            left = helper(root.left)
            right = helper(root.right)

            Min = min(left[0], right[0])
            Max = max(left[1], right[1])

            self.max_diff = max(self.max_diff, max(abs(root.val - Min), abs(root.val - Max)))

            Min = min(Min, root.val)
            Max = max(Max, root.val)

            return [Min, Max]
        
        helper(root)
        return self.max_diff
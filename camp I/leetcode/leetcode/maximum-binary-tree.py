# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return

        i = nums.index(max(nums))
        left = self.constructMaximumBinaryTree(nums[:i])
        right = self.constructMaximumBinaryTree(nums[i + 1:])
        root = TreeNode(nums[i], left, right)
        return root
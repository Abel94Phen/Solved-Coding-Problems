# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.hashmap = {}
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root):
            if root:
                self.hashmap[root.val] = self.hashmap.get(root.val, 0) + 1
                traverse(root.left)
                traverse(root.right)
        
        traverse(root)
        mode = max(self.hashmap.values())
        result = []
        
        for key,val in self.hashmap.items():
            if val == mode:
                result.append(key)
        return result
        


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.hashtable = defaultdict(list)

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        def traverse(root, row, col):
            if not root:
                return
            
            self.hashtable[col].append((root.val, row))
            traverse(root.left, row + 1, col - 1)
            traverse(root.right, row + 1, col + 1)
            
        traverse(root, 0, 0)
        Keys = list(self.hashtable.keys())
        Keys.sort()
        result = []

        for Key in Keys:
            List = self.hashtable[Key]
            List.sort(key = lambda x : (x[1], x[0]))
            column = []
            for i in range(len(List)):
                column.append(self.hashtable[Key][i][0])
            result.append(column)
        
        
        return result
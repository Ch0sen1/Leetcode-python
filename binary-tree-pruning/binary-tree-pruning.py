# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = self.dfs(root)
        return root if not res else None
        
    def dfs(self, root):
        if not root:
            return True
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        
        if l:
            root.left = None
        if r:
            root.right = None
            
        return l and r and root.val == 0
        
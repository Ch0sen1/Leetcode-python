# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.dfs(root, root)
        return self.count
        
    
    def dfs(self, root, parent):
        if not root:
            return True
        l = self.dfs(root.left, root)
        r = self.dfs(root.right, root)
        if l and r:
            self.count += 1
        return l and r and root.val == parent.val
        
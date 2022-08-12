# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.res = True
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if not root:
            return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        if abs(l-r) > 1:
            self.res = False
        return max(l,r)+1
        
        
        
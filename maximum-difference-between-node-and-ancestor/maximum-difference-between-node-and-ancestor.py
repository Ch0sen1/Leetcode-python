# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        
        return self.dfs(root, root.val, root.val)
        
    def dfs(self, root, high, low):
        if not root:
            return high - low
        
        l = self.dfs(root.left, max(high, root.val), min(low, root.val))
        r = self.dfs(root.right, max(high, root.val), min(low, root.val))
        
        return max(l, r)
        
        
        
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = float("-inf")
        self.dfs(root)
        return self.max
    
    def dfs(self, root):
        if not root:
            return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        self.max = max(self.max, (max(l,0)+max(r,0)+root.val))
        
        return max(l, r, 0) + root.val
        
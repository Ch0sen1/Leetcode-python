# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res
    
    
    def dfs(self, root):
        if not root:
            return 0
        length = 1
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        if root.left and root.left.val == root.val + 1:
            length = max(length, l+1)
        if root.right and root.right.val == root.val + 1:
            length = max(length, r+1)
        self.res = max(self.res, length)
        
        return length
        
        
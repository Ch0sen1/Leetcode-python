# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        return self.dfs(root, p ,q)
        
        
    def dfs(self, root, p, q):
        if not root:
            return None
        if root == p or root == q:
            return root
        l = self.dfs(root.left, p, q)
        r = self.dfs(root.right, p ,q)
        
        if l and r:
            return root
        elif l:
            return l
        elif r:
            return r
        
        
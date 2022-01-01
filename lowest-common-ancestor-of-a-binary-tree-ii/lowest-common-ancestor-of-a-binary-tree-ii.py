# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = self.dfs(root, p, q)
        ## make sure the node is in the nde
        result1 = self.dfs(root, p, p)
        result2 = self.dfs(root, q, q)
        
        if result1 and result2:
            return result
        else:
            return None
    
    
    def dfs(self, root, p, q):
        if not root:
            return None
        if root == p or root == q:
            return root
        l = self.dfs(root.left, p, q)
        r = self.dfs(root.right, p, q)
        
        if (l and r):
            return root
        
        return l if l else r
        
        
        
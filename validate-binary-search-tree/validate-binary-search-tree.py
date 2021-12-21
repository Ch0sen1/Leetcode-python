# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('inf'), float('-inf'))
        
    
    def dfs(self, root, max_val, min_val):
        if not root:
            return True
        
        if min_val < root.val < max_val:
            return (self.dfs(root.left, root.val, min_val) and self.dfs(root.right, max_val, root.val))
        else:
            return False
        
        
        
        
        
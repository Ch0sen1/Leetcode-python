# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        height, bal = self.dfs(root, True)
        return bal
        
    
    def dfs(self, root, bal):
        if not root:
            return 0, True
        l,lb = self.dfs(root.left, bal)
        r,rb = self.dfs(root.right, bal)
        
        bal = None
        if abs(l-r) > 1 or rb == False or lb == False:
            bal = False
        else:
            bal = True
        
        return max(l,r)+1, bal
        
        
        
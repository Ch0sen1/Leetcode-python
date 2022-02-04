# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        self.res = None
        self.dfs(root,p)
        return self.res
        
    
    
    def dfs(self, root, p):
        if not root:
            return None
        if p.val < root.val:
            self.res = root
            self.dfs(root.left, p)
        else:
            self.dfs(root.right, p)
        
        
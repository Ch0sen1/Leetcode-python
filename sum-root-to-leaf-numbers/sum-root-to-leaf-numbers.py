# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root, "")
        return self.res
        
    def dfs(self, root, path):
        if not root:
            return
        if not root.left and not root.right:
            total = int(path+str(root.val))
            self.res += total
        
        self.dfs(root.left, path+str(root.val))
        self.dfs(root.right, path+str(root.val))
        
        return
        
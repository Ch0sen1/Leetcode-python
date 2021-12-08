# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res
        
    
    def dfs(self, root):
        if not root:
            return 0
        left_value = self.dfs(root.left)
        right_value = self.dfs(root.right)
        self.res += abs(left_value - right_value)
        return left_value + right_value + root.val
        
        
    
        
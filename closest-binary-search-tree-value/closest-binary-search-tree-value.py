# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.closet = root.val
        self.dfs(root, target)
        return self.closet
    
    def dfs(self, root, target):
        if not root:
            return None
        if abs(root.val - target) < abs(self.closet- target):
            self.closet = root.val
        if root.val > target:
            self.dfs(root.left, target)
        if root.val < target:
            self.dfs(root.right, target)
        
        return root
        
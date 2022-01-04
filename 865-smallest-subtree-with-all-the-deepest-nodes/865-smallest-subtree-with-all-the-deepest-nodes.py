# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self.dfs(root, 0)[0]
        
    def dfs(self, root, depth):
        if not root:
            return None, depth
        left, leftDepth = self.dfs(root.left, depth+1)
        right, rightDepth = self.dfs(root.right, depth+1)
        
        if leftDepth > rightDepth:
            return left, leftDepth
        elif rightDepth > leftDepth:
            return right, rightDepth
        else:
            return root, leftDepth
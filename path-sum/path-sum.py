# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root,targetSum,[],res)
        return len(res) > 0
    
    def dfs(self, root, targetSum, path, res):
        if not root:
            return
        if targetSum == root.val and (not root.left) and (not root.right):
            path.append(root.val)
            res.append(path)
            return
        self.dfs(root.left, targetSum - root.val, path+[(root.val)],res)
        self.dfs(root.right, targetSum - root.val, path+[(root.val)],res)
        
            
        
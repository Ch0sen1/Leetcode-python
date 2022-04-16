# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.val = []
        self.s = 0
    
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.val.append(root.val)
            inorder(root.right)
            
        inorder(root)
        
        
        def rdfs(root):
            if not root:
                return
            rdfs(root.right)
            self.s += self.val.pop()
            root.val = self.s
            rdfs(root.left)
        
        rdfs(root)
        
        return root
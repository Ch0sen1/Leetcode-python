# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        fromArray = []
        self.inorder(root, fromArray)
        return self.buildBinaryTree(fromArray, 0, len(fromArray)-1)
        
    
    def inorder(self, root, fromArray):
        if not root:
            return
        self.inorder(root.left, fromArray)
        fromArray.append(root.val)
        self.inorder(root.right, fromArray)
    
    
    ## pass in is the index
    def buildBinaryTree(self, array, low, high):
        if low > high:
            return None
        mid = (low + high) // 2
        root = TreeNode(array[mid])
        root.left = self.buildBinaryTree(array, low, mid-1)
        root.right = self.buildBinaryTree(array, mid+1, high)
        return root
        
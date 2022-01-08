# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        v = []
        self.getArray(root, v)
        return self.buildTreeArray(0, len(v)-1, v)
        
        
        
    def getArray(self, root, array):
        if not root:
            return
        self.getArray(root.left, array)
        array.append(root.val)
        self.getArray(root.right, array)
        return
    
    def buildTreeArray(self, low, high, array):
        if low > high:
            return
        mid = (low + high) // 2
        root = TreeNode(array[mid])
        root.left = self.buildTreeArray(low, mid-1, array)
        root.right = self.buildTreeArray(mid+1, high, array)
        return root
        
        
        
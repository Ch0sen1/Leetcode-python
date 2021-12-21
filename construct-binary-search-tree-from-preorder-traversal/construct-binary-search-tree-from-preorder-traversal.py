# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
            
        root = TreeNode(preorder[0])
        
        # index = self.findNextGreaterIndex(preorder, root.val)
        index = bisect.bisect(preorder, preorder[0])
        root.left = self.bstFromPreorder(preorder[1:index])
        root.right = self.bstFromPreorder(preorder[index:])
        
        return root
        
    def findNextGreaterIndex(self, nums, val):
        for i in range(len(nums)):
            if nums[i] > val:
                return i
                
        
        
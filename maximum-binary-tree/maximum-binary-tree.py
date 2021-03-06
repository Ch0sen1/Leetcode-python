# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        max_val_index = nums.index(max(nums))
        root = TreeNode(max(nums))
        
        root.left = self.constructMaximumBinaryTree(nums[:max_val_index])
        root.right = self.constructMaximumBinaryTree(nums[max_val_index+1:])
        
        return root
        
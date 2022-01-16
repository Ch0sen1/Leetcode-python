# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1, list2 = deque(), deque()
        res = []
        self.inorder(root1, list1)
        self.inorder(root2, list2)
        
        while list1 and list2:
            res.append(list1.popleft() if list1[0] < list2[0] else list2.popleft())
        return res + list(list1) + list(list2)
        
        
        
        
    def inorder(self, root, array):
        if not root:
            return
        self.inorder(root.left, array)
        array.append(root.val)
        self.inorder(root.right, array)
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        if root:
            q.append(root)
        while q:
            size = len(q)
            levelMax = q[0].val
            for i in range(size):
                node = q.popleft()
                levelMax = max(levelMax, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(levelMax)
            
        return res
            
        
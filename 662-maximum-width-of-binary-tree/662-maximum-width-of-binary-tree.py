# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxWidth = 0
        q = deque()
        if root:
            q.append((root, 0, 0))
            
        while q:
            maxWidth = max((q[-1][2] - q[0][2]),maxWidth)
            for _ in range(len(q)):
                node, level, pos = q.popleft()
                # dic[level].append(pos)
                if node.left:
                    q.append((node.left, level+1, pos*2))
                if node.right:
                    q.append((node.right, level+1, pos*2+1))
        
        
        return maxWidth + 1
            
                
                    
                
            
        
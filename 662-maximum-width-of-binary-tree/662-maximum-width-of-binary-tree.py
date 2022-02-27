# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dic = defaultdict(list)
        maxWidth = 0
        q = deque()
        if root:
            q.append((root, 0, 0))
            
        while q:
            for _ in range(len(q)):
                node, level, pos = q.popleft()
                dic[level].append(pos)
                if node.left:
                    q.append((node.left, level+1, pos*2))
                if node.right:
                    q.append((node.right, level+1, pos*2+1))
        
        for level in dic:
            maxWidth = max(max(dic[level]) - min(dic[level]), maxWidth)
        
        return maxWidth + 1
            
                
                    
                
            
        
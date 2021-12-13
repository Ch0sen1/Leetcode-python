# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dic = collections.defaultdict(list)
        queue = collections.deque()
        maxWidth = 0
        if root:
            queue.append([root, 0 ,0])
        while queue:
            size = len(queue)
            for _ in range(size):
                node, level, pos = queue.popleft()
                dic[level].append(pos)
                if node.left:
                    queue.append([node.left, level+1, pos*2])
                if node.right:
                    queue.append([node.right, level+1, pos*2+1])
        for level in dic:
            maxWidth = max(max(dic[level]) - min(dic[level]), maxWidth)
        return maxWidth + 1
                
                    
                
            
        
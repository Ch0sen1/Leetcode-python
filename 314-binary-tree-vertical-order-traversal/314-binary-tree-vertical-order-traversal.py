# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        leveldict = defaultdict(list)
        
        q = deque()
        if not root:
            return res
        
        q.append((root, 0))
        
        while q:
            size = len(q)
            for _ in range(size):
                node, level = q.popleft()
                leveldict[level].append(node)
                if node.left:
                    q.append((node.left, level-1))
                if node.right:
                    q.append((node.right, level+1))
        
        for level, nodes in sorted(leveldict.items()):
            new = []
            for node in nodes:
                new.append(node.val)
            res.append(new)
        
        return res
                
        
            
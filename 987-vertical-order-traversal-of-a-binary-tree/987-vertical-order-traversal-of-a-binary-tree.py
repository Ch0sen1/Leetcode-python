# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        res = []
        q = collections.deque()
        if root:
            q.append((root, 0, 0))
        
        while q:
            size = len(q)
            for _ in range(size):
                node, pos, level = q.popleft()
                dic[pos].append((level, node.val))
                if node.left:
                    q.append((node.left, pos-1, level+1))
                if node.right:
                    q.append((node.right, pos+1, level+1))
        
        for pos in sorted(dic.keys()):
            new = []
            for val in sorted(dic[pos]):
                new.append(val[1])
            res.append(new)
            
        return res
                
            
        
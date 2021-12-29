# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.res = []
        self.matchParent(root, None)
        self.seen = set()
        self.k = k
        self.countDist(target, 0)
        return self.res
        
    
    
    def matchParent(self, root, parent):
        if not root:
            return
        root.parent = parent
        self.matchParent(root.left, root)
        self.matchParent(root.right, root)
        
    def countDist(self, root, dist):
        if not root or dist > self.k or root in self.seen:
            return
        self.seen.add(root)
        if dist == self.k:
            self.res.append(root.val)
            return
        self.countDist(root.parent, dist+1)
        self.countDist(root.left, dist+1)
        self.countDist(root.right, dist+1)
        
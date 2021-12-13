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
        queue = collections.deque()
        if root:
            queue.append([root,0,0])
        while queue:
            size = len(queue)
            for _ in range(size):
                node, pos, curLevel = queue.popleft()
                dic[pos].append((curLevel, node.val))
                if node.left:
                    queue.append([node.left, pos-1, curLevel+1])
                if node.right:
                    queue.append([node.right, pos+1, curLevel+1])
        
        for i in sorted(dic.keys()):
            temp = []
            ## sorted by level
            for j in sorted(dic[i]):
                # only append the value into the res
                temp.append(j[1])
            res.append(temp)
        return res
            
        
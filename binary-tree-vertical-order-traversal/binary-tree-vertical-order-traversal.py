# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = collections.defaultdict(list)
        queue = collections.deque()
        if root:
            queue.append([root, 0])
        while queue:
            node, pos = queue.popleft()
            res[pos].append(node.val)
            if node.left:
                queue.append([node.left, pos - 1])
            if node.right:
                queue.append([node.right, pos + 1])
        
        return [res[i] for i in sorted(res)]
        
            
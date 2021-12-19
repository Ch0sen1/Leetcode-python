# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        res = []
        queue = collections.deque()
        if root:
            queue.append(root)
        while queue:
            node = queue.popleft()
            if node is None:
                res.append('n')
                continue
            else:
                res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        return ','.join(res)
            
                
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        queue = collections.deque()
        queue.append(root)
        index = 1
        while queue:
            node = queue.popleft()
            if nodes[index] != 'n':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1
            
            if nodes[index] != 'n':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
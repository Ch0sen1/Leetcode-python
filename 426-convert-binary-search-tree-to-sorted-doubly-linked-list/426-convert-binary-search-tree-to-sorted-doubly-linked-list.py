"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        
        stack = []
        node = root
        
        dummy = Node(0, None, None)
        prev = dummy
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.left, prev.right, prev = prev, node, node
            node = node.right
        
        
        # now node = 5
        dummy.right.left, prev.right = prev, dummy.right
        
        return dummy.right
        
        
            
            
        
        
            
    
    
        
        
        
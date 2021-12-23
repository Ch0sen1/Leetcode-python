"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldNodeToCopyNode = {None: None}
        
        cur = head
        while cur:
            copy = Node(cur.val)
            oldNodeToCopyNode[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldNodeToCopyNode[cur]
            copy.next = oldNodeToCopyNode[cur.next]
            copy.random = oldNodeToCopyNode[cur.random]
            
            cur = cur.next
            
        return oldNodeToCopyNode[head]
        
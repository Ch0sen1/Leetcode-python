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
        old_to_new = defaultdict()
        old_to_new[None] = None
        
        cur = head
        
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next
            
        cur = head
        
        while cur:
            node = old_to_new[cur]
            node.next = old_to_new[cur.next]
            node.random = old_to_new[cur.random]
            cur = cur.next
            
        return old_to_new[head]
            
        
        
        
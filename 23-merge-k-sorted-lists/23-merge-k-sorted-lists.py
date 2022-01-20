# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
    
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(0)
        cur = head
        nodes = []
        
        ListNode.__lt__ = lambda self, other: self.val < other.val
        
        for node in lists:
            if node:
                heapq.heappush(nodes,(node.val, node))
            
            
        while len(nodes) > 0:
            val, node = heapq.heappop(nodes)
            cur.next = node
            if node.next:
                heapq.heappush(nodes,(node.next.val, node.next))
            cur = node
        
        return head.next
            
            
        
        
        
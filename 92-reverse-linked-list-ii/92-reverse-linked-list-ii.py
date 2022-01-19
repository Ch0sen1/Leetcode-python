# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre = dummy
        
        
        
        # reverse the node of [m,n] then connect m-1 to n and connect m to n+1
        
        # get m-1
        for i in range(left-1):
            pre = pre.next
        
        cur = pre.next
        
        
        tmp = None
        for i in range(right - left + 1):
            nxt = cur.next
            cur.next = tmp
            tmp = cur
            cur = nxt
        
        pre.next.next = cur
        pre.next = tmp
        
        return dummy.next
            
        
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = dummy = ListNode(0, head)
        cur = head
        while cur:
            ## have duplicate
            if cur and cur.next and cur.val == cur.next.val:
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur.next
                cur = cur.next
            
            ## no duplicate
            else:
                pre = cur
                cur = cur.next
        
        return dummy.next
            
            
        
        
                
            
                
        
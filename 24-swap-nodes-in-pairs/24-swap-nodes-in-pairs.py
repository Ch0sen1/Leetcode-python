# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = pre = ListNode(0)
        dummy.next = head
        
        
        while head and head.next:
            
            tmp = head.next
            head.next = tmp.next
            pre.next = tmp
            tmp.next = head
            head = head.next
            pre = tmp.next
        
        return dummy.next
            
            
        
        
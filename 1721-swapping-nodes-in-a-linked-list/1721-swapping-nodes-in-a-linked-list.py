# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 :
            return head
        dummy = preLeft = preRight = ListNode(-1, head)
        right = left = head
        
        for _ in range(k-1):
            preLeft = preLeft.next
            left = left.next
            
        
        fast = left
            
        while fast.next:
            preRight = preRight.next
            right = right.next
            fast = fast.next
            
        
        # perform swap
        
        
        preLeft.next, preRight.next = right, left
        left.next, right.next = right.next, left.next
        
        return dummy.next
        
        
        
        
            
        
        
        
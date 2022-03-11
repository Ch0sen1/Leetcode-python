# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head == None:
            return head
        
        dummy = ListNode(0, head)
        tail = dummy
        temp = dummy
        n = 0
        
        # get the length and get the last element
        while tail.next:
            n += 1
            tail = tail.next
            
        if k == 0:
            k = 0
        else:
            k = k % n
        
        for _ in range(n-k):
            temp = temp.next
        
        
        tail.next = dummy.next
        dummy.next = temp.next
        temp.next = None
        
        return dummy.next
        
        
        
        
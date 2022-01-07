# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        

    def getRandom(self) -> int:
        count = 0
        cur = self.head
        res = None
        
        while cur:
            count += 1
            chance = random.randint(1, count)
            if chance == 1:
                res = cur.val
            cur = cur.next
        
        return res
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
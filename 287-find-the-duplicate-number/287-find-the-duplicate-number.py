class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        check = 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
            
        
        while check != slow:
            slow = nums[slow]
            check = nums[check]
        
        return slow
            
        
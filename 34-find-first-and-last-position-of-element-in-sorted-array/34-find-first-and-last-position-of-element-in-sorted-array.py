class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        l = self.searchlower(nums, target)
        r = self.searchlower(nums, target + 1) -1
        
        if l <= r:
            return [l, r]
        
        return [-1, -1]
            
        
    
    def searchlower(self, nums, target):
        l = 0
        r = len(nums)
        while l < r:
            mid = (l+r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l
        
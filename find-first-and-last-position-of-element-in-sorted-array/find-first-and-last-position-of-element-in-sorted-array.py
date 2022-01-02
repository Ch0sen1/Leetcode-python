class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = self.searchlower(nums, target), self.searchhiger(nums, target) - 1
        return [
            left if left < len(nums) and nums[left] == target else -1,
            right if 0 <= right < len(nums) and nums[right] == target else -1
        ]
        
        
    
    def searchlower(self, nums, target):
        l = 0
        r = len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        return l
    
    
    def searchhiger(self, nums, target):
        l = 0
        r = len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        
        return l
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        l = 0
        r = len(nums)
        while l < r:
            mid = (l+r) //2
            if nums[mid] - nums[0] - mid < k:
                l = mid + 1
            else:
                r = mid
        
        
        return nums[l-1] + (k - (nums[l-1] - nums[0] - (l-1)))
        
        
        
    
    
#     def countMissing(self, nums, i):
        
#         return nums[i] - nums[0] - i
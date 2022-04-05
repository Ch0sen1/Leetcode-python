class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        
        max_area = 0
        
        
        while l < r:
            
            area = min(nums[l], nums[r]) * (r - l)
            max_area = max(area, max_area)
            if nums[l] > nums[r]:
                r -= 1
            else:
                l += 1
        
        return max_area
        
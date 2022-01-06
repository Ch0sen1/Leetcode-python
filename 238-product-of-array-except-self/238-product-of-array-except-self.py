class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        
        res = [0] * len(nums)
        
        for i in range(len(nums)):
            res[i] = p
            p = nums[i] * p
        
        p = 1
        
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * p
            p = nums[i] * p
        
        
        return res
            
            
            
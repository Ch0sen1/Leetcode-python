class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        res = [0] * len(nums)
        
        for i in range(len(nums)):
            res[i] = p
            p = p * nums[i]
        
        # after first iteration
        # [1,1,2,6]
        p = 1
        
        for i in range(len(nums)-1, -1, -1):
            res[i] = p * res[i]
            p = p * nums[i]
        
        return res
            
        
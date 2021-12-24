class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        p = 1
        for i in range(len(nums)):
            res.append(p)
            p = p * nums[i]
        
        p = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * p
            p = p * nums[i]
        
        return res
            
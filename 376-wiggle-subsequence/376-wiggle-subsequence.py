class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        up = None
        res = 1
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 0 and up != False:
                res += 1
                up = False
            elif nums[i] - nums[i-1] < 0 and up != True:
                res += 1
                up = True
            
        return res
            
            
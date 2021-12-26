class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        ## first mark all the negative back to zero
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = 0
        
        ## transfrom the pointing index into negative value
        for i in range(len(nums)):
            # this line is trying to avoid [0 - 1]  nums[-1] to be change
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] = - nums[val - 1]
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)
                    
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
                    
            
        return len(nums) + 1    
        
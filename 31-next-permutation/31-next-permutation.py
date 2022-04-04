class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # find first number that are greater than previous
        
        i = j = k = len(nums) - 1
        
        while i > 0 and nums[i] <= nums[i-1] :
            i -= 1
        
        if i == 0:
            nums.reverse()
            return
        
        nums_swap = i - 1
        
        while j > 0 and nums[j] <= nums[nums_swap]:
            j -= 1
            
        nums[nums_swap], nums[j] = nums[j], nums[nums_swap]
        
        
        while i < k:
            nums[i], nums[k] = nums[k], nums[i]
            i += 1
            k -= 1
            
        return
        
        
        
        
        
        
        
        
        
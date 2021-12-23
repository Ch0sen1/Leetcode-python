class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = r = len(nums) - 1
        
        
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        if i == 0:
            nums.reverse()
            return
        
        k = i - 1
        
        while nums[j] <= nums[k]:
            j -= 1
        
        nums[k], nums[j] = nums[j], nums[k]
        
        
        while i < r:
            nums[i], nums[r] = nums[r],nums[i]
            i += 1
            r -= 1

        
        
        
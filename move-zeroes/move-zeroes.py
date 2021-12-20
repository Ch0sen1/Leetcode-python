class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_zero = 0
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[last_zero] = nums[last_zero], nums[i]
                last_zero += 1
            i += 1
                
                
                
        
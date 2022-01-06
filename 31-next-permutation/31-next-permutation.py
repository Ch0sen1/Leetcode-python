class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
            
        if i == 0:
            nums.reverse()
            return
        
        swap_item = i - 1
        
        j = len(nums) - 1
        
        while j > 0 and nums[j] <= nums[swap_item]:
            j -= 1
            
        nums[swap_item], nums[j] = nums[j], nums[swap_item]
        
        k = len(nums) - 1
        while i < k:
            nums[i], nums[k] = nums[k], nums[i]
            i += 1
            k -= 1
            
        return 
            

        
        
        
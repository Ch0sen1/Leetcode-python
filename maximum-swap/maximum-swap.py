class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        i = 0
        j = len(nums) - 1
        while i < len(nums)-1:
            if nums[i] < nums[i+1]:
                break
            i += 1
        
        if i == len(nums) - 1:
            return num
        
        max_idx = i+1
        max_value = nums[i+1]
        for j in range(i+1, len(nums)):
            if nums[j] >= max_value:
                max_idx = j
                max_value = nums[j]
                
                
        min_idx = i
        for j in range(i, -1, -1):
            if nums[j] < max_value:
                min_idx = j
                
        nums[max_idx], nums[min_idx] = nums[min_idx], nums[max_idx]
            
        
        return int(''.join(nums))
        
        
            
        
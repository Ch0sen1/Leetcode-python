class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start = 0
        end = 0
        maxend = 0
        step = 0
        
        if len(nums) <= 1:
            return 0
        #actually, while True
        while end < n-1:
            step += 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
            
                
                
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        
        
        s = set(nums)
        
        for i, num in enumerate(nums):
            curLong = 1
            
            j = 1
            while (num+j) in s:
                s.remove(num+j)
                j += 1
                curLong += 1
            
            j = 1
            
            while (num-j) in s:
                s.remove(num-j)
                j += 1
                curLong += 1
            
            res = max(curLong, res)
        
        return res
            
            
            
        
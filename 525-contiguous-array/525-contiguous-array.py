class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0:0}
        count = 0
        res = 0
        
        for i, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if count in dic:
                res = max(res, i - dic[count])
            else:
                dic[count] = i
        
        return res
                
            
                
                
        
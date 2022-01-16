class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        maxSize = 0
        total = 0
        c = Counter()
        c[0] = -1
        
        for i, num in enumerate(nums):
            total += num
            
            if (total - k) in c:
                maxSize = max(maxSize, (i- c[total-k]))
            if total not in c:
                c[total] = i
        
        return maxSize
                
        
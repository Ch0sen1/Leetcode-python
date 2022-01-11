class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = Counter()
        total = 0
        c[total] += 1
        cnt = 0
        for num in nums:
            total += num
            cnt += c[total - k]
            c[total] += 1
            
        
        return cnt
            
            
        
        
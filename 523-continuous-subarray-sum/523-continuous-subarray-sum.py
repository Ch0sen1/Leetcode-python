class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total = 0
        c = Counter()
        c[0] = -1
        
        for i, num in enumerate(nums):
            total += num
            mod = total % k
            
            if mod not in c:
                c[mod] = i
            else:
                if i - c[mod] >= 2:
                    return True
        return False
            
            
        
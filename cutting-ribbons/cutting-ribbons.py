class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        if sum(ribbons) < k:
            return 0
        
        def canCut(num):
            cnt = 0
            for r in ribbons:
                cnt += r // num
            return cnt >= k
                
        ## bisect right
        l = 1
        r = max(ribbons)
        
        while l <= r:
            mid = (l+r) // 2
            if canCut(mid):
                l = mid + 1
            else:
                r = mid - 1
            
        return l - 1
            
        
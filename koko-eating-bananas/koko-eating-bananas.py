class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAll(mid):
            total = 0
            for pile in piles:
                total += ceil(pile/mid)
            return total <= h   
        
        l = 1
        r = max(piles)
        
        while l < r:
            mid = (l+r)//2
            if canEatAll(mid) != True:
                l = mid + 1
            else:
                r = mid
        
        return l
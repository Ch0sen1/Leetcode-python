class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        
        
        while l < r:
            mid = (l+r) // 2
            if self.canEatAll(piles, h, mid) != True:
                l = mid + 1
            else:
                r = mid
        return l    
            
    
    def canEatAll(self, piles, h, k):
        total = 0
        for pile in piles:
            total += ceil(pile/k)
        return total <= h
            
class Solution:

    def __init__(self, w: List[int]):
        
        for i in range(1, len(w)):
            w[i] = w[i] +w[i-1]
            
        self.weightSum = w
        
    def pickIndex(self) -> int:
        # probability of pibkcing W[I] / sum(w)
        idx = random.randint(1, self.weightSum[-1])
        l = 0
        r = len(self.weightSum)
        
        while l < r:
            mid = (l+r) // 2
            if self.weightSum[mid] < idx:
                l = mid + 1
            else:
                r = mid
        return l
        
        
        


class Solution:
    def sumZero(self, n: int) -> List[int]:
        extend = n // 2
        even = n % 2
        
        if even == 0:
            res = []
        else:
            res = [0]
        
        
        for i in range(1, extend+1):
            res.append(i)
            res.append(-i)
        
        return res
            
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        self.even_mid = ['11','69','88','96','00']
        self.odd_mid = ['0','1','8']
        return self.dfs(n)
        
    def dfs(self, n):
        if n == 1:
            return self.odd_mid
        elif n == 2:
            return self.even_mid[:-1]
        elif n % 2 == 1:
            pre, mid_candidate = self.dfs(n-1), self.odd_mid
        else:
            pre, mid_candidate = self.dfs(n-2), self.even_mid
        
        res = []
        premid = (n-1)//2
        
        for p in pre:
            for m in mid_candidate:
                res.append(p[:premid] + m + p[premid:])
        return res
        
        
            
        
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.dfs(x, -n)
        else:
            return self.dfs(x, n)
    
    
    def dfs(self, x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        half = self.dfs(x, n//2)
        
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
        
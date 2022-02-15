class Solution:
    # @lru_cache(None)
    # def climbStairs(self, n: int) -> int:
    #     if n <= 1:
    #         return 1
    #     else:
    #         return self.climbStairs(n-1) + self.climbStairs(n-2)
        
        
    def climbStairs(self, n):
        dp = [1] * (n+1)
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        
        
        
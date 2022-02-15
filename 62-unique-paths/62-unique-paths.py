class Solution:
    # @lru_cache(None)
    # def uniquePaths(self, m: int, n: int) -> int:
    #     if m <= 0 or n <= 0:
    #         return 0
    #     if m == 1 and n == 1:
    #         return 1
    #     return self.uniquePaths(m-1,n) + self.uniquePaths(m, n-1)
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (m+1) for _ in range(n+1)]
        dp[1][1] = 1
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] += dp[i-1][j] + dp[i][j-1]
        
        return dp[n][m]
    
        
        
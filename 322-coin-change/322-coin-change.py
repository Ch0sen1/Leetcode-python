class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        
        def dp(num):
            if num == 0:
                return 0
            ans = float('inf')
            for c in coins:
                if num - c >= 0:
                    ans = min(ans, dp(num - c)+1)
            return ans
        
        return dp(amount) if dp(amount)!= float('inf') else -1
                    
            
        
        
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dp = {}
        arr.sort()
        dp[arr[0]] = 1
        n = 10**9 +7
        
        for num in arr:
            ans = 1
            for cand in arr:
                if num % cand == 0 and num // cand in arr:
                    ans += dp[cand] *dp[(num//cand)]
            dp[num] = ans
        
        res = 0
        for val in dp.values():
            res += val
        
        return res % n
                    
                    
                    
            
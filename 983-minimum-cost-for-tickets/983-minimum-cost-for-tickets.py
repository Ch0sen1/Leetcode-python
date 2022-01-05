class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0 for i in range(days[-1]+1)]
        
        for i in range(days[-1]+1):
            if i not in days:
                dp[i] = dp[i-1]
            else:
              # We select the min cost for 3 cases in travel day:
              #1. the accumulated cost in 1-day ago + the cost of 1-day pass;
              #2. the accumulated cost in 7-day ago + the cost of 7-day pass;
              #3. the accumulated cost in 30-day ago + the cost of 30-day pass.
                dp[i] = min(
                dp[max(0, i-1)]+costs[0], 
                dp[max(0, i-7)]+costs[1], 
                dp[max(0,i-30)] + costs[2]
                )
        
        return dp[days[-1]]
        
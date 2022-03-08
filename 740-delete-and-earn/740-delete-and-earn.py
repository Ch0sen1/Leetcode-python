class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = Counter(nums)
        total_point = [0] * (max(nums) + 1)
        
        for key, value in c.items():
            total_point[key] = key * value
        
        return self.houseRobber(total_point)
        
    def houseRobber(self, houses):
        
        dp = [0] * len(houses)
        if len(houses) == 0:
            return 0
        if len(houses) == 1:
            return houses[1]
        if len(houses) == 2:
            return max(houses)
        
        dp[1] = houses[1]
        
        for i in range(2, len(houses)):
            dp[i] = max((dp[i-2] + houses[i]), dp[i-1])
        
        return dp[len(houses)-1]
            
            
        
            
            
        
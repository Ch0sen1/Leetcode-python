class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        totalSum = sum(nums)
        if totalSum % k != 0:
            return False
        targetSum = totalSum / k
        visited = [False] * len(nums)
        return self.dfs(nums, visited, targetSum, 0, k, 0)
        
    
    def dfs(self, nums, visited, targetSum, curSum, k, start):
        if k == 1:
            return True
        if curSum == targetSum:
            return self.dfs(nums, visited, targetSum, 0, k-1, 0)
        
            
        for i in range(start, len(nums)):
            if visited[i] != True and curSum + nums[i] <= targetSum:
                visited[i] = True
                if self.dfs(nums, visited, targetSum, curSum+nums[i], k, i + 1):
                    return True
                visited[i] = False
        return False
        
        
        
        
        
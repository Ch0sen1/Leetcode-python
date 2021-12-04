class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False
        subset_sum = nums_sum / k
        ks = [0] * k
        nums.sort(reverse=True)
        visited = [False] * len(nums)
        return self.dfs(nums, visited, 0, k, 0, subset_sum)
        
    def dfs(self, nums, visited, start, k, curSum, targetSum):
        if k == 1:
            return True
        if curSum == targetSum:
            return self.dfs(nums, visited, 0, k - 1, 0, targetSum)
        
        for i in range(start, len(nums)):
            if not visited[i] and curSum + nums[i] <= targetSum:
                visited[i] = True
                if self.dfs(nums, visited, i + 1, k, curSum+nums[i], targetSum):
                    return True
                visited[i] = False
        
        return False
        
        
        
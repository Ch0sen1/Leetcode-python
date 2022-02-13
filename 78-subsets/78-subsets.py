class Solution:
    def subsets(self, nums):
        res = []
        self.dfs(0, [], res, nums)
        return res
        
    def dfs(self, index, path, res, nums):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(i+1, path+[nums[i]], res, nums)
    
        
        
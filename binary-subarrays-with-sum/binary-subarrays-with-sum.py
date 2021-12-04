class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.atMostK(nums,goal) - self.atMostK(nums,goal-1)
        
        
    def atMostK(self, nums, goal):
        if goal < 0: return 0
        l = r = res = 0
        c = collections.Counter()
        while r < len(nums):
            goal -= nums[r]
            while l < len(nums) and goal < 0:
                goal += nums[l]
                l += 1
            res += r - l + 1
            r += 1
        return res
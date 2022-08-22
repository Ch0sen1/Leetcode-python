class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMostK(nums, k):
            if k < 0 :
                return 0
            l = r = res = 0
            total = 0
            while r < len(nums):
                total += nums[r]
                while l <len(nums) and total > k:
                    total -= nums[l]
                    l += 1
                res += r-l+1
                r += 1
            return res
        
        
        
        return atMostK(nums,goal) - atMostK(nums,goal-1)
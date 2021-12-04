class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k-1)
    
    def atMostK(self, nums, k):
        l = r = res = 0
        c = collections.Counter()
        while r < len(nums):
            c[nums[r]] += 1
            while len(c) > k:
                c[nums[l]] -= 1
                if c[nums[l]] == 0:
                    del c[nums[l]]
                l += 1
            res += r - l + 1
            r += 1
        return res
            
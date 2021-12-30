class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = res = 0
        d = collections.Counter()
        res = 0
        while r < len(nums):
            d[nums[r]] += 1
            while d[0] > k:
                d[nums[l]] -= 1
                l += 1
            res = max(res, r-l+1)
            r+=1
        return res
            
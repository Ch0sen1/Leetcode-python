class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = res = 0
        d = collections.Counter()
        # expand window
        while r < len(nums):
            d[nums[r]] += 1
            # shrink window
            while d[0] > k:
                d[nums[l]] -= 1
                l += 1
            r += 1
            res = max(res, r - l)
        return res
            
        
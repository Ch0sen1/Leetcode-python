class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        res = len(nums) + 1
        total = 0
        while r < len(nums):
            total += nums[r]
            while total >= target:
                res = min(res, r-l+1)
                total -= nums[l]
                l += 1
            r += 1
        return res if res <= len(nums) else 0
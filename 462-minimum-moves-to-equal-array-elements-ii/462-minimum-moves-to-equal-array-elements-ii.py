class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = len(nums)//2
        res = 0
        for num in nums:
            res += abs(num - nums[median])
        return res
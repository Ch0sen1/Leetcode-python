class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        return self.atMostK(fruits,2)
        
        
    def atMostK(self, nums, k):
        l = r = res = 0
        c = Counter()
        while r < len(nums):
            c[nums[r]] += 1
            while len(c) > 2:
                c[nums[l]] -= 1
                if c[nums[l]] == 0:
                    del c[nums[l]]
                l += 1
            res = max(res, r-l + 1)
            r += 1
        return res
        
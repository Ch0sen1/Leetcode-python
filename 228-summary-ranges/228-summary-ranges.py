class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        l = 0
        i = 0
        res = []
        while i < len(nums) - 1:
            # range stop
            if nums[i]+1 != (nums[i+1]):
                res.append(self.helper(nums[l], nums[i]))
                l = i + 1
            i += 1
        res.append(self.helper(nums[l], nums[i]))
        return res
        
        
        
    def helper(self, l, r):
        if l == r:
            return str(l)
        else:
            return str(l) + "->" + str(r)
            
        
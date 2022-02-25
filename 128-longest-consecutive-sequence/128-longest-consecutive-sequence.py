class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set(nums)
        for num in nums:
            curLong = 1
            j = 1
            while (num - j) in s:
                s.remove(num - j)
                j += 1
                curLong += 1
            j = 1
            
            while (num + j) in s:
                s.remove(num + j)
                j += 1
                curLong += 1
            
            longest = max(curLong, longest)
            
        return longest
        
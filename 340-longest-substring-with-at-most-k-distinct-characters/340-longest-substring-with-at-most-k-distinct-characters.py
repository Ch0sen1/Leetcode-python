class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        c = Counter()
        l = r = 0
        res = 0
        while r < len(s):
            c[s[r]] += 1
            while len(c) > k:
                c[s[l]] -= 1
                if c[s[l]] == 0:
                    del c[s[l]]
                l += 1
            res = max(res, r - l + 1)
            r += 1
            
        return res
            
        
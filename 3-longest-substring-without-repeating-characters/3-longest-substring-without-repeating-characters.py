class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        res = 0
        have = Counter()
        while r < len(s):
            have[s[r]] += 1
            while self.helperCheck(have):
                have[s[l]] -= 1
                if have[s[l]] == 0:
                    del have[s[l]]
                l += 1
            res = max(res, r-l+1)
            r += 1
        
        return res
            
            
    def helperCheck(self, m):
        for value in m.values():
            if value > 1:
                return True
        return False
        
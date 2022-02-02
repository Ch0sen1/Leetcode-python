class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = Counter(p)
        have = Counter()
        res = []
        
        l = 0
        r = 0
        
        while r < len(s):
            have[s[r]] += 1
            while r - l + 1 > len(p):
                have[s[l]] -= 1
                if have[s[l]] == 0:
                    del have[s[l]]
                l += 1
            if need == have:
                res.append(l)
            
            r += 1
        return res
            
            
            
            
        
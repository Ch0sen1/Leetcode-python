class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        c = Counter()
        l = r = 0
        while r < len(s):
            word = s[r]
            c[word] += 1
            while(r-l+1 - max(c.values()) > k):
                c[s[l]] -= 1
                l += 1
            res = max(r-l+1, res)
            r += 1
        return res
                
        
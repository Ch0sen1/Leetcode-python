class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        needWord = Counter(p)
        haveWord = Counter()
        l = r = 0
        while r < len(s):
            haveWord[s[r]] += 1
            while r - l >= len(p):
                haveWord[s[l]] -= 1
                if haveWord[s[l]] == 0:
                    del haveWord[s[l]]
                l += 1
            if needWord == haveWord:
                res.append(l)
            r += 1
        return res
            
            
        
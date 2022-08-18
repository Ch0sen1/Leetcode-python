class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        need = Counter(t)
        l = r = 0
        while r < len(s):
            word = s[r]
            need[word] -= 1
            while all(value <= 0 for value in need.values()) and l <= r:
                if res == "":
                    res = s[l:r+1]
                elif (r-l+1) < len(res):
                    res = s[l:r+1]
                
                need[s[l]] += 1
                l += 1
            r += 1
        return res
        
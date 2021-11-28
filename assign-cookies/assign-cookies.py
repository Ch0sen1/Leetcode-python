class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        p1 = 0
        p2 = 0
        res = 0
        while True:
            if p1 >= len(g) or p2 >= len(s):
                break
            if s[p2] >= g[p1]:
                p2 += 1
                p1 += 1
                res += 1
            elif g[p1] > s[p2]:
                p2 += 1
        return res
        
            
        
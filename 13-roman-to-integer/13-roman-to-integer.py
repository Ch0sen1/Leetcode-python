class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'M': 1000, 'D':500, 'C':100,'L':50,'X':10,'V':5,'I':1}
        res = 0
        prev = None
        
        for i ,c in enumerate(s):
            if prev:
                if dic[s[i]] > dic[s[i-1]]:
                    res += (dic[s[i]] - 2*(dic[s[i-1]]))
                    continue
            res += dic[s[i]]
            prev = c
        
        return res
            
            
        
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        tmp = k
        res = ""
        count = 0
        for i in range(len(s)):
            if s[i].isalnum():
                count += 1
        for i in range(len(s)-1,-1,-1):
            c = s[i]
            if count == 0:
                return res
            if tmp == 0:
                res = '-' + res
                tmp = k
            if c == '-':
                continue
            else:
                if c.isalpha:
                    c = c.upper()
                res = c + res
                tmp -= 1
                count -= 1
        return res
                
                
                
            
        
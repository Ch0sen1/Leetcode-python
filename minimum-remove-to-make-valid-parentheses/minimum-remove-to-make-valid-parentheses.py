class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        j = -1
        res = ""
        for i, c in enumerate(s):
            if c == '(':
                j = max(j+1, i+1)
                while j < len(s) and s[j] != ')':
                    j +=1
                
                if j < len(s) and s[j] == ')':
                    res += c
                
            elif c == ')':
                if i <= j:
                    res += c
                    
            else:
                res += c
            
        
        
        return res
                
        
                
            
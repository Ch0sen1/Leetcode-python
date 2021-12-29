class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        
        if s == t:
            return False
        
        if max(len_s,len_t) - min(len_s, len_t) > 1:
            return False
        
        i = j = edit = 0
        
        while i < len_s and j < len_t:
            
            if s[i] == t[j]:
                i += 1
                j += 1
                
            else:
                edit += 1
                if edit == 2:
                    return False
                if len_s > len_t:
                    i += 1
                elif len_t > len_s:
                    j += 1
                else:
                    i +=1
                    j += 1
        
        
        return True
                    
                
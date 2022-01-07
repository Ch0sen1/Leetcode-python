class Solution:
    def customSortString(self, S: str, T: str) -> str:
        c = Counter(T)
        res = ""
        for ch in S:
            if ch in c:
                res += ch * c.pop(ch)
            
        
        for key, value in c.items():
            res += key * value
        
        return res
            
            
        
        
            
        
            
        
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        C = Counter(T)
        res = ""
        for s in S:
            if s in C:
                res += s * C.pop(s)
        for key, value in C.items():
            res += key * value
        
        return res
            
        
        
            
        
            
        
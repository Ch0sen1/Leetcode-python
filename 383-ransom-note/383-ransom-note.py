class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = Counter(ransomNote)
        g = Counter(magazine)
        
        for key, values in c.items():
            if key not in magazine:
                return False
            elif c[key] > g[key]:
                return False
        
        return True
        
        
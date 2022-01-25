class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = Counter(s)
        
        
        for i, char in enumerate(t):
            if char in c:
                c[char] -= 1
            else:
                c[char] += 1
        
        for key, value in c.items():
            if value != 0:
                return False
        
        return True
        
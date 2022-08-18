class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for i in range(len(queries)):
            if self.check(queries[i], pattern):
                res.append(True)
            else:
                res.append(False)
        return res
        
    def check(self, word, pattern):
        j = 0
        for i, c in enumerate(word):
            if j < len(pattern) and c == pattern[j]:
                j += 1
            elif c.isupper():
                return False
        
        return j == len(pattern)
                
        
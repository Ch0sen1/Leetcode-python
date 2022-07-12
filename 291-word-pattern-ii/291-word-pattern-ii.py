class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        c = Counter()
        return self.dfs(pattern, s, c)
        
        
    def dfs(self, pattern, s, dic):
        if len(s) == 0 and len(pattern) == 0:
            return True
        if len(s) == 0 or len(pattern) == 0:
            return False
        for i in range(1, len(s)-len(pattern)+2):
            word = s[:i]
            p = pattern[0]
            if p not in dic and word not in dic.values():
                dic[p] = word
                if self.dfs(pattern[1:], s[i:], dic):
                    return True
                del dic[p]
            elif p in dic and dic[p] == word:
                if self.dfs(pattern[1:], s[i:], dic):
                    return True
        
        return False
            # if p not in dic:
            #     if word not in dic.values(): 
            #         dic[p] = word
            #         if self.dfs(pattern[1:], s[i:], dic):
            #             return True
            #         del dic[p]
            # else:
            #     if dic[p] != word:
            #         return False
            #     else:
            #         if self.dfs(pattern[1:], s[i:], dic):
            #             return True
        return False
            
            
                
            
        
        
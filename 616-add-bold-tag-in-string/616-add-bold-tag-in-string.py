class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        status = [False] * len(s)
        res = ""
        for word in words:
            l = s.find(word)
            
            while l != -1:
                for i in range(l, l+len(word)):
                    status[i] = True
                l = s.find(word, l+1)
        
        i = 0
        while i < len(s):
            if status[i]:
                res += "<b>"
                while i < len(s) and status[i]:
                    res += s[i]
                    i += 1
                res += "</b>"
            else:
                res += s[i]
                i += 1
        return res
            
                
                    
        
        
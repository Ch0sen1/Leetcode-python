class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        status = [False] * len(s)
        res = ""
        
        for word in words:
            start = s.find(word)
            
            while start != -1:
                for j in range(start, start+len(word)):
                    status[j] = True
                start = s.find(word, start+1)
        
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
                    
        
        
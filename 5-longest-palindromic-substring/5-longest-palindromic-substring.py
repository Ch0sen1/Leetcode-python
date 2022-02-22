class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            tmp = self.checkPalindrome(s,i,i)
            if len(tmp) > len(res):
                res = tmp
            tmp = self.checkPalindrome(s,i,i+1)
            if len(tmp) > len(res):
                res = tmp
            
        
        return res
        
        
    
    
    
    def checkPalindrome(self, s, i ,j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1:j]
        
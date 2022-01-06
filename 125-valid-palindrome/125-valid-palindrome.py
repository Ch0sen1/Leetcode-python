class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for c in s.lower():
            if c.isalnum():
                res += c
                
        return res == res[::-1]
            
        
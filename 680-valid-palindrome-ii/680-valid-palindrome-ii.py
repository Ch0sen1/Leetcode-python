class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        k = 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if k:
                    word1 = s[l+1:r+1]
                    word2 = s[l:r]
                    return word1 == word1[::-1] or word2 == word2[::-1]
                else:
                    return False
        
        return True
            
        
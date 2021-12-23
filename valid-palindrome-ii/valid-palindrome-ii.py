class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        k = 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if k:
                    new_s1, new_s2 = s[l+1:r+1], s[l:r]
                    return new_s1 == new_s1[::-1] or new_s2 == new_s2[::-1]
                    k -= 1
                else:
                    return False
        
        return True
            
        
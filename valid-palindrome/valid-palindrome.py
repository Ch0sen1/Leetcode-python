class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s.lower():
            if i.isalnum():
                res += i
        return res[::-1] == res
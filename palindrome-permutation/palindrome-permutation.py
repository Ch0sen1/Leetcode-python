class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        c = Counter(s)
        haveOne = 0
        for key,value in c.items():
            if value % 2 == 1:
                haveOne += 1
            if haveOne >= 2:
                return False
        return True
        
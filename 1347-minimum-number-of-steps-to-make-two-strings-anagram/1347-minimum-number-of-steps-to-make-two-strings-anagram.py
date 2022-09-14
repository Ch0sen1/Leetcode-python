class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        c = Counter(s)
        res = 0
        for word in t:
            if c[word] >= 1:
                c[word] -= 1
            else:
                res += 1
        return res
        
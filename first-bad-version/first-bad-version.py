# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid) != True:
                l = mid + 1
            else:
                r = mid - 1
            # shrink to the left
            # so if mid
        
        return l
        
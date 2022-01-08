class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        res = 0
        for age in ages:
            l = bisect.bisect_right(ages, 0.5*age +7)
            r = bisect.bisect_right(ages, age)
            
            res += max(0, (r - l) - 1)
        
        return res
            
            
            
        
        
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        c = Counter(ages)
        res = 0
        for age1, count1 in c.items():
            for age2, count2 in c.items():
                ## in range of the friend request, two people send two request to another people = 4
                if age2 > 0.5 * age1 + 7 and (age2 <= age1):
                    res += count1 * count2
                    ## avoid duplicate calculation
                    if age1 == age2:
                        res -= count1
        
        return res
            
            
        
        
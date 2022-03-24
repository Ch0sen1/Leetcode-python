class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse = True)
        l = 0
        r = len(people) - 1
        res = 0
        
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
                res += 1
            else:
                l += 1
                res += 1
        return res
        
        
        
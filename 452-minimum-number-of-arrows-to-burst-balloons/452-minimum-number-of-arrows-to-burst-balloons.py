class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        prev = float("-inf")
        points = sorted(points, key = lambda x:x[1])
        arrow = 0
        for start, end in points:
            if start > prev:
                arrow += 1
                prev = end
                
        return arrow
            
        
            
        
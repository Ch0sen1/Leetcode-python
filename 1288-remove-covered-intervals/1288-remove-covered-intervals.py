class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: (i[0], -i[1]))
        prev = 0
        res = 0
        
        for start, end in intervals:
            if end > prev:
                res += 1
                prev = end
            else:
                continue
        
        return res
            
                      
        
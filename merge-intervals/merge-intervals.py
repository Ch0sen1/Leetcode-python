class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        # when will they intersect :  a_end > b_start
        for i in range (len(intervals)):
            if res == []:
                res.append(intervals[i])
            else:
                a_start = res[-1][0]
                a_end = res[-1][1]
                b_start = intervals[i][0]
                b_end = intervals[i][1]
                
                # have intersected
                if a_end >= b_start:
                    res[-1][1] = max(a_end, b_end)
                else:
                    res.append(intervals[i])
        return res
            
            
        
        
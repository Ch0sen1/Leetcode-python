class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
            else:
                prev_start, prev_end = res[-1]
                cur_start, cur_end = intervals[i]
                if cur_start <= prev_end and prev_start <= cur_end:
                    res[-1][1] = max(cur_end, prev_end)
                else:
                    res.append(intervals[i])
                    
        return res
            
            
        
        
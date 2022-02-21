class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        for start, end in sorted(intervals, key = lambda i:i[0]):
            if not res:
                res.append([start, end])
            else:
                prev_start = res[-1][0]
                prev_end = res[-1][1]
                # when do we overlap?  when cur_start come before prev_end
                if start <= prev_end:
                    res[-1][0] = min(prev_start, start)
                    res[-1][1] = max(prev_end, end)
                else:
                    res.append([start, end])
        
        return res
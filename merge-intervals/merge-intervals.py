class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for i in intervals:
            if res == []:
                res.append(i)
            else:
                ## when to merge? when b_start <= res_end
                res_start = res[-1][0]
                res_end = res[-1][1]
                
                b_start = i[0]
                b_end = i[1]
                
                if b_start <= res_end:
                    res[-1][1] = max(res_end, b_end)
                else:
                    res.append(i)
        return res
            
            
        
        
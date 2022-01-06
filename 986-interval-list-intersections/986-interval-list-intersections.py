class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []
        
        # when do we have interval?
        # when A[start] <= B[end] and B[start] <= A[end]
        # interval = A[end] - B[start]
        
        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]    
            
            if a_start <= b_end and b_start <= a_end:
                res.append([max(a_start, b_start), min(a_end, b_end)])
            if a_end <= b_end:
                i += 1
            else:
                j += 1         
        return res
        
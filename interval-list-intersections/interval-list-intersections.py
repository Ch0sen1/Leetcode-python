class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i = 0
        j = 0
        
        # two pointer apporach
        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]
            
            # make sure they are overlap in some part
            if a_start <= b_end and b_start <= a_end:
                res.append([max(a_start, b_start), min(a_end, b_end)])
            # move pointer, over comapre overlapping
            # if a_start <= b_start, it means first one is smaller, so can move
            if a_end <= b_end:
                i += 1
            else:
                j += 1
        return res
                
                
        
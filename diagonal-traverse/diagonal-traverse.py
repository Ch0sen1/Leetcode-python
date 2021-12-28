class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        dic = defaultdict(list)
        reverse = True
        res = []
        
        for i in range(rows):
            for j in range(cols):
                dic[(i+j)].append(mat[i][j])
        
        for key, value in dic.items():
            if reverse:
                for v in value[::-1]:
                    res.append(v)
            else:
                for v in value:
                    res.append(v)
            reverse = not reverse
        
        return res
                
                    
            
        
        
        
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        res = []
        c = defaultdict(list)
        reverse = True
        
        # travese the mat, c[key] is i+j unique
        for i in range(rows):
            for j in range(cols):
                c[i+j].append(mat[i][j])
            
        for key, value in c.items():
            if key % 2 == 0:
                for element in value[::-1]:
                    res.append(element)
            else:
                for element in value:
                    res.append(element)
            
            
                    
        return res
                
                    
            
        
        
        
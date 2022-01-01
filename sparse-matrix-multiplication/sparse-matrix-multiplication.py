class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        
        if A is None or B is None: return None
        # g aka k
        m, g = len(A), len(A[0])
        # if len(b) is not equal to k, return
        if len(B) != g:
            return
        
        # k * n : n
        n = len(B[0])
        
        table_A, table_B = defaultdict(), defaultdict()
        
        for i, row in enumerate(A):
            for j, val in enumerate(row):
                if val:
                    if i not in table_A:
                        table_A[i] = defaultdict()
                    table_A[i][j] = val
        
        for i, row in enumerate(B):
            for j, val in enumerate(row):
                if val:
                    if i not in table_B:
                        table_B[i] = defaultdict()
                    table_B[i][j] = val
                    
        C = [[0 for j in range(n)] for i in range (m)]
        
        for i in table_A:
            for k in table_A[i]:
                if k not in table_B: continue
                for j in table_B[k]:
                    C[i][j] += table_A[i][k] * table_B[k][j]
                
        
        
        return C
        
        
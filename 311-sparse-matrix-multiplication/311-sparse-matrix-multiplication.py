class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return None
        m = len(A)
        k = len(A[0])
        if len(B) != k:
            return 
        n = len(B[0])
        
        dicA = defaultdict()
        dicB = defaultdict()
        
        # for i in range(m):
        #     for j in range(k):
        #         if A[i][j]:
        #             if i not in dicA:
        #                 dicA[i] = defaultdict()
        #             dicA[i][j] = A[i][j]
                    
        # for i in range(k):
        #     for j in range(n):
        #         if B[i][j]:
        #             if k not in dicB:
        #                 dicB[i] = defaultdict()
        #             dicB[i][j] = B[i][j]
        
        for i, row in enumerate(A):
            for j, val in enumerate(row):
                if val:
                    if i not in dicA:
                        dicA[i] = defaultdict()
                    dicA[i][j] = val
        
        for i, row in enumerate(B):
            for j, val in enumerate(row):
                if val:
                    if i not in dicB:
                        dicB[i] = defaultdict()
                    dicB[i][j] = val
                    
        C = [[0 for _ in range(n)] for _ in range(m)]
        
        for mm in dicA:
            for kk in dicA[mm]:
                if kk not in dicB: continue
                for nn in dicB[kk]:
                    C[mm][nn] += dicA[mm][kk] * dicB[kk][nn]
                    
        return C
                    
                    
        
        
         
        
        
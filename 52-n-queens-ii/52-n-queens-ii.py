class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        posDia = set()
        negDia = set()
        
        res = []
        
        board = [['.' for _ in range(n)] for _ in range(n)]
        
        
        def dfs(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r+c) in posDia or (r-c) in negDia:
                    continue
                
                cols.add(c)
                posDia.add(r+c)
                negDia.add(r-c)
                board[r][c] = 'Q'
                
                dfs(r+1)
                
                cols.remove(c)
                posDia.remove(r+c)
                negDia.remove(r-c)
                board[r][c] = '.'
        
        dfs(0)
        return len(res)
        
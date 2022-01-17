class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return []
        
        self.rows = len(board)
        self.cols = len(board[0])
        self.dirs = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
        
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        self.dfs(click[0], click[1], board)
        
        return board
    
    def dfs(self, i, j, board):
        if board[i][j] != 'E':
            return
        
        mine_count = 0
        
        for dx,dy in self.dirs:
            newx, newy = i + dx, j + dy
            if 0 <= newx < self.rows and 0 <= newy < self.cols and board[newx][newy] == 'M':
                mine_count += 1
        
        if mine_count == 0:
            board[i][j] = 'B'
        else:
            board[i][j] = str(mine_count)
            return
        
        for dx,dy in self.dirs:
            newx, newy = i + dx, j + dy
            if 0 <= newx < self.rows and 0 <= newy < self.cols:
                self.dfs(newx, newy, board)
        
        
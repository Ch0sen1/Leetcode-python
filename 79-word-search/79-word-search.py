class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i, j, board, word):
                    return True
        return False
        
    def dfs(self, x, y, board, word):
        if len(word) == 0:
            return True
        if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == word[0]:
            tmp = board[x][y]
            board[x][y] = "!"
            for dx, dy in self.dirs:
                newx, newy = x + dx, y + dy
                if self.dfs(newx, newy, board, word[1:]):
                    return True
            board[x][y] = tmp
        return False
    
    
                
        
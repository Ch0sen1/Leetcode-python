class TicTacToe:

    def __init__(self, n: int):
        self.ans = n
        self.row = [0] * n
        self.col = [0] * n
        self.dig = [0] * 2
        

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.row[row] += 1
            self.col[col] += 1
            if row == col:
                self.dig[0] += 1
            if row + col == self.ans - 1:
                self.dig[1] += 1
            if self.row[row] == self.ans or self.col[col] == self.ans or self.dig[0] == self.ans or self.dig[1] == self.ans:
                return 1
        else:
            self.row[row] -= 1
            self.col[col] -= 1
            if row == col:
                self.dig[0] -= 1
            if row + col == self.ans - 1:
                self.dig[1] -= 1
            if self.row[row] == -(self.ans) or self.col[col] == -(self.ans) or self.dig[0] == -(self.ans) or self.dig[1] == -(self.ans):
                return 2
        return 0
            
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        
        self.sums = [[0 for j in range(cols+1)]  for i in range(rows+1)]
        
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                self.sums[i][j] = matrix[i-1][j-1] + self.sums[i-1][j] + self.sums[i][j-1] - self.sums[i-1][j-1]
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        result = self.sums[row2][col2] - self.sums[row1-1][col2] - self.sums[row2][col1-1] + self.sums[row1-1][col1-1]
        return result
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
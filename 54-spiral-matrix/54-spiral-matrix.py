class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height = len(matrix)
        width = len(matrix[0])
        
        left = 0
        right = width - 1
        top = 0
        bottom = height - 1
        
        res = []
        
        while left < right and top < bottom:
            for col in range(left, right):
                res.append(matrix[top][col])
                
            for row in range(top, bottom):
                res.append(matrix[row][right])
            
            for col in range(right, left, -1):
                res.append(matrix[bottom][col])
            
            for row in range(bottom, top, -1):
                res.append(matrix[row][left])
            
            top += 1
            bottom -= 1
            left += 1
            right -= 1
            
        
        if len(res) < height * width:
            for i in range(top, bottom+1):
                for j in range(left, right+1):
                    res.append(matrix[i][j])
        
        return res
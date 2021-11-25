class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        l = 0 
        r = len(matrix) * cols - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid//cols][mid%cols] == target:
                return True
            elif matrix[mid//cols][mid%cols] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
        
        
        
                
                
        
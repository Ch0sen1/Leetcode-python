# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        res = cols
        
        for row in range(rows):
            l = 0
            r = cols
            while l < r:
                mid = (l + r) // 2
                if binaryMatrix.get(row, mid) < 1:
                    l = mid + 1
                else:
                    r = mid
            res = min(res, l)
            
        return res if res < cols else -1
            
                    
            
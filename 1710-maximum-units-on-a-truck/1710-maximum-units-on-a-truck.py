class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda x:x[1], reverse = True)
        res = 0
        for key,value in boxTypes:
            if key <= truckSize:
                res += key * value
                truckSize -= key
            else:
                res += truckSize * value
                return res
        
        return res
                
        
        
        
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if start < 0 or start >= len(arr) or arr[start] < 0:
            return False
        
        if arr[start] == 0:
            return True
        
        arr[start] = -arr[start]
        try1 = self.canReach(arr, start+arr[start])
        try2 = self.canReach(arr, start-arr[start])
        arr[start] = -arr[start]
        
        return try1 or try2
        
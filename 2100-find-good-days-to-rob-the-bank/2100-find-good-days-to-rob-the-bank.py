class Solution:
    def goodDaysToRobBank(self, arr: List[int], time: int) -> List[int]:
        # before i need to be non-increasing arr[i] <= arr[i-1]
        # after i need to be non-decreasing arr[i] >= arr[i+1]
        
        monoDecrease = [0] * len(arr)
        monoIncrease = [0] * len(arr)
        res = []
        
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                monoDecrease[i] = monoDecrease[i-1] + 1
        
        for i in range(len(arr)-2, -1, -1):
            if arr[i] <= arr[i+1]:
                monoIncrease[i] = monoIncrease[i+1] + 1
        
        for i in range(len(arr)):
            if monoDecrease[i] >= time and monoIncrease[i] >= time:
                res.append(i)
        
        return res
                
        
            
            
        
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        target = [total/4] * 4
        matchsticks.sort(reverse = True)
        
        return self.dfs(matchsticks, 0, target)
        
    def dfs(self, arr, idx, target):
        if idx == len(arr):
            return True
        for i in range(4):
            if target[i] >= arr[idx]:
                target[i] -= arr[idx]
                if self.dfs(arr, idx+1, target):
                    return True
                target[i] += arr[idx]
        
        return False
            
            
            
        
        
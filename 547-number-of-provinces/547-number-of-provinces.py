class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        visited = set()
        
        
        def dfs(node):
            for i, val in enumerate(isConnected[node]):
                if val == 1 and i not in visited:
                    visited.add(i)
                    dfs(i)
        
        
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                res += 1
        
        return res
        
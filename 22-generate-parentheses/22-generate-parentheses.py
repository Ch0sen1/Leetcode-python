class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(n, n, "", res)
        return res
        
        
        
        
    def dfs(self, left, right, path, res):
        
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > right or left < 0 or right < 0:
            return
        self.dfs(left-1, right, path+'(', res)
        self.dfs(left, right-1, path+')', res)
        
        
        
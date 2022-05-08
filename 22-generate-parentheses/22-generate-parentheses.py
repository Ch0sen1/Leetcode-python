class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(n, n, "", res)
        return res
    
    def dfs(self, right, left, path, res):
        if right == 0 and left == 0:
            res.append(path)
            return
        if right > left or right < 0 or left < 0:
            return
        self.dfs(right - 1, left, path+ '(', res)
        self.dfs(right, left - 1, path+ ')', res)
        
        
        
        
        
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        self.target = target
        res = []
        for i in range(1, len(num)+1):
            if i == 1 or (i > 1 and num[0] != '0'):
                self.dfs(num[i:], int(num[:i]), int(num[:i]), num[:i], res)
        return res
        
        
    def dfs(self, num, cur, last, temp, res):
        if not num:
            if cur == self.target:
                res.append(temp)
            return
        for i in range(1, len(num)+1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != '0'):
                self.dfs(num[i:], cur+int(val), int(val), temp+'+'+val, res)
                self.dfs(num[i:], cur-int(val), -int(val), temp+'-'+val, res)
                self.dfs(num[i:], cur-last+last*int(val), last*int(val), temp+'*'+val, res)
            
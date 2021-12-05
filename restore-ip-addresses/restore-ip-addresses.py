class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.dfs(s, res, "", 0)
        return res
        
    def dfs(self, s, res, path, idx):
        if idx > 4:
            return 
        if idx == 4 and not s:
            res.append(path[:-1])
            return
        for i in range(1, len(s)+1):
            if s[:i] == '0' or (s[0] != '0' and 0 < int(s[:i]) < 256):
                self.dfs(s[i:], res, path+s[:i]+".", idx+1)
            
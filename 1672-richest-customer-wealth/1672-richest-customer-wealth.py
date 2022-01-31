class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for i in range(len(accounts)):
            temp = 0
            for j in range(len(accounts[0])):
                temp += accounts[i][j]
            
            maxWealth = max(maxWealth, temp)
        
        return maxWealth
                
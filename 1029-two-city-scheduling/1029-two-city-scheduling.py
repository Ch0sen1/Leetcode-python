class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        res = 0
        refund = [0] * len(costs)
        
        for i in range(len(costs)):   
            res += costs[i][0]
            refund[i] = costs[i][1] - costs[i][0]
        
        n = len(costs) // 2
        refund = sorted(refund)
        
        for i in range(n):
            res += refund[i]
            
        return res            
            
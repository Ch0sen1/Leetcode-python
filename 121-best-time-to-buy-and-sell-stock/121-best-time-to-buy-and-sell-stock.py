class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = float("-inf")
        minPrice = prices[0]
        for price in prices:
            minPrice = min(minPrice, price)
            curProfit = price - minPrice
            maxProfit = max(maxProfit, curProfit)
        
        return maxProfit
        
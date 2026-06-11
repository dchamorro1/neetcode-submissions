class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxCurrentProfit = 0
        minBuy = prices[0]

        for price in prices:
            minBuy = min(minBuy, price)
            maxCurrentProfit = max(maxCurrentProfit, price - minBuy)

        return maxCurrentProfit
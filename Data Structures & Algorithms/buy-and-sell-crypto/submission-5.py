class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximumProfit = 0
        minBuy = prices[0]

        # our minBuy is initialized to prices[0]

        # iterate through each value in prices. At each stage we calcualte the maxProfit and the Minimum Buy.
        # keep highestMaxSell and return it at the end

        for price in prices:
            maximumProfit = max(maximumProfit, price - minBuy)
            minBuy = min(minBuy, price)

        return maximumProfit
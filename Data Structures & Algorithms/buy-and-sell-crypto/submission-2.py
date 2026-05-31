class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        maxGrowth = 0

        while r < len(prices):
            # if price at r is less than price at l then our new l is equal to r. (New lowest l)
            currentGrowth = prices[r] - prices[l]
            maxGrowth = max(currentGrowth, maxGrowth)
            
            if prices[r] < prices[l]:
                l = r
            else:
                r += 1

        return maxGrowth



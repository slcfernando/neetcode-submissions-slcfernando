class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        maxProfit = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[l] <= prices[r]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r = l + 1

        return maxProfit
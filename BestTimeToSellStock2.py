class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        start_price = prices[0]

        for i in range(0, len(prices)):
            if prices[i] > start_price:
                max_profit += prices[i] - start_price
            start_price = prices[i]
        return max_profit
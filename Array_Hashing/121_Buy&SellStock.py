class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_price = prices[0]
        for price in prices:
            current_price  = min(current_price,price)
            profit = price - current_price
            max_profit = max(max_profit,profit)
        return max_profit
        
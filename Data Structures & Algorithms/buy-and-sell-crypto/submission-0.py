class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 1000
        sell = 0
        profit = 0
        for price in prices:
            sell = price
            buy = min(buy, price)
            profit = max(profit, sell-buy)
        return profit
        

        
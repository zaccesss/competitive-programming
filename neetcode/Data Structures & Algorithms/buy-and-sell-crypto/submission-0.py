class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Lowest buying price seen so far
        min_price = prices[0]

        # Maximum profit found
        max_profit = 0

        # Start from second day
        for price in prices[1:]:

            # Profit if sold today
            profit = price - min_price

            # Update maximum profit
            max_profit = max(max_profit, profit)

            # Update lowest buying price
            min_price = min(min_price, price)

        return max_profit
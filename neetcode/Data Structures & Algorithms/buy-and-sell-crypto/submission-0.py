class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # lowest buying price seen so far
        min_price = prices[0]

        # maximum profit found
        max_profit = 0

        # start from second day
        for price in prices[1:]:

            # profit if sold today
            profit = price - min_price

            # update maximum profit
            max_profit = max(max_profit, profit)

            # update lowest buying price
            min_price = min(min_price, price)

        return max_profit
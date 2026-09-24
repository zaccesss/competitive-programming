class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # store total profit
        profit = 0

        # loop through the list starting from index 1
        for i in range(1, len(prices)):

            # if today's price is greater than yesterday's
            if prices[i] > prices[i - 1]:

                # add the difference to profit
                profit += prices[i] - prices[i - 1]

        # return total profit
        return profit
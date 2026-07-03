class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Store total profit
        profit = 0

        # Loop through the list starting from index 1
        for i in range(1, len(prices)):

            # If today's price is greater than yesterday's
            if prices[i] > prices[i - 1]:

                # Add the difference to profit
                profit += prices[i] - prices[i - 1]

        # Return total profit
        return profit
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculate the maximum profit you can achieve by buying and selling stock on the same day.

        Args:
            prices (List[int]): The list of stock prices for each day.

        Returns:
            int: The maximum profit achievable.
        """
        max_profit = 0  # Initialize the maximum profit to 0

        for i in range(1, len(prices)):
            # Calculate the profit for the current day (buying and selling on the same day)
            profit = prices[i] - prices[i - 1]

            # If the profit is positive, add it to the maximum profit
            if profit > 0:
                max_profit += profit

        return max_profit

        
class Solution:
    def maxProfit(self, prices):
        """
        Find the maximum profit with at most two transactions given an array of stock prices.

        :param prices: List of stock prices for each day.
        :type prices: List[int]
        :return: Maximum profit achievable.
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0

        # Initialize variables to track the maximum profit with two transactions.
        buy1, buy2 = -prices[0], -prices[0]
        sell1, sell2 = 0, 0

        for i in range(1, n):
            # Update the first buy and sell considering the current price.
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])

            # Update the second buy and sell considering the current price and the profit from the first transaction.
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])

        # The maximum profit is achieved by selling at the end.
        return sell2

# Example usage:
prices1 = [3, 3, 5, 0, 0, 3, 1, 4]
solution = Solution()
result1 = solution.maxProfit(prices1)
print(result1)  # Output: 6

prices2 = [1, 2, 3, 4, 5]
result2 = solution.maxProfit(prices2)
print(result2)  # Output: 4

prices3 = [7, 6, 4, 3, 1]
result3 = solution.maxProfit(prices3)
print(result3)  # Output: 0
   
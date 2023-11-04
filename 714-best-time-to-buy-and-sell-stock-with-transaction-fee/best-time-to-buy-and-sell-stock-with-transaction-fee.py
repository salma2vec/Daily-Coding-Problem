class Solution:
    def maxProfit(self, prices, fee):
        """
        Find the maximum profit given an array of stock prices with a transaction fee.

        :param prices: List of stock prices for each day.
        :type prices: List[int]
        :param fee: Transaction fee for each transaction.
        :type fee: int
        :return: Maximum profit achievable.
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0

        # Initialize buy and sell arrays to track the best actions on each day.
        buy = [-prices[0]] + [0] * (n - 1)
        sell = [0] * n

        for i in range(1, n):
            buy[i] = max(sell[i - 1] - prices[i], buy[i - 1])
            sell[i] = max(buy[i - 1] + prices[i] - fee, sell[i - 1])

        # The maximum profit is achieved by selling on the last day.
        return sell[n - 1]

# Example usage:
prices1 = [1, 3, 2, 8, 4, 9]
fee1 = 2
solution = Solution()
result1 = solution.maxProfit(prices1, fee1)
print(result1)  # Output: 8

prices2 = [1, 3, 7, 5, 10, 3]
fee2 = 3
result2 = solution.maxProfit(prices2, fee2)
print(result2)  # Output: 6

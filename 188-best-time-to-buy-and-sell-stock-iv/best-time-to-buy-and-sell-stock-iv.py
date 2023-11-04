class Solution:
    def maxProfit(self, k, prices):
        """
        Find the maximum profit with at most k transactions given an array of stock prices.

        :param k: Maximum number of transactions allowed.
        :type k: int
        :param prices: List of stock prices for each day.
        :type prices: List[int]
        :return: Maximum profit achievable.
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0

        # If the number of transactions allowed is greater than or equal to half the number of days, we can do as many transactions as we want.
        if k >= n // 2:
            max_profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    max_profit += prices[i] - prices[i - 1]
            return max_profit

        # Initialize two lists to keep track of the buy and sell states for each day.
        buy = [-float('inf')] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for i in range(1, k + 1):
                # Update the buy and sell states considering the current price.
                buy[i] = max(buy[i], sell[i - 1] - price)
                sell[i] = max(sell[i], buy[i] + price)

        # The maximum profit is achieved by selling at the end.
        return sell[k]

# Example usage:
k1 = 2
prices1 = [2, 4, 1]
solution = Solution()
result1 = solution.maxProfit(k1, prices1)
print(result1)  # Output: 2

k2 = 2
prices2 = [3, 2, 6, 5, 0, 3]
result2 = solution.maxProfit(k2, prices2)
print(result2)  # Output: 7

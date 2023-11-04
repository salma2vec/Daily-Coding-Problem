class Solution:
    def maxProfit(self, prices):
        """
        Find the maximum profit given an array of stock prices with cooldown.
        
        :param prices: List of stock prices for each day.
        :type prices: List[int]
        :return: Maximum profit achievable.
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        
        # Initialize buy, sell, and cooldown arrays to track the best actions on each day.
        buy = [-prices[0]] + [0] * (n - 1)
        sell = [0] * n
        cooldown = [0] * n
        
        for i in range(1, n):
            buy[i] = max(cooldown[i - 1] - prices[i], buy[i - 1])
            sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])
            cooldown[i] = max(sell[i - 1], cooldown[i - 1])
        
        # The maximum profit is achieved by either selling or in cooldown on the last day.
        return max(sell[n - 1], cooldown[n - 1])

# Example usage:
prices1 = [1, 2, 3, 0, 2]
solution = Solution()
result1 = solution.maxProfit(prices1)
print(result1)  # Output: 3

prices2 = [1]
result2 = solution.maxProfit(prices2)
print(result2)  # Output: 0

        
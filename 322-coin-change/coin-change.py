class Solution:
    def coinChange(self, coins, amount):
        """
        Return the fewest number of coins needed to make up the given amount.

        :param coins: List of coin denominations.
        :type coins: List[int]
        :param amount: Total amount of money to make up.
        :type amount: int
        :return: Fewest number of coins needed, or -1 if it's not possible.
        :rtype: int
        """
        # Create a list to store the fewest number of coins for each amount from 0 to the target amount.
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # It takes 0 coins to make up an amount of 0.

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

# Example usage:
coins1 = [1, 2, 5]
amount1 = 11
coins2 = [2]
amount2 = 3
coins3 = [1]
amount3 = 0

solution = Solution()
result1 = solution.coinChange(coins1, amount1)  # Output: 3
result2 = solution.coinChange(coins2, amount2)  # Output: -1
result3 = solution.coinChange(coins3, amount3)  # Output: 0

print(result1)
print(result2)
print(result3)

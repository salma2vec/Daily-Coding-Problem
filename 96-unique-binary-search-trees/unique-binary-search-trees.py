class Solution:
    def numTrees(self, n):
        """
        Calculate the number of structurally unique BSTs with n nodes.

        :param n: Number of nodes.
        :type n: int
        :return: Number of structurally unique BSTs.
        :rtype: int
        """
        if n <= 1:
            return 1

        # Initialize a list to store the number of unique BSTs for each number of nodes.
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                dp[nodes] += dp[root - 1] * dp[nodes - root]

        return dp[n]

# Example usage:
n1 = 3
solution = Solution()
result1 = solution.numTrees(n1)
print(result1)  # Output: 5

n2 = 1
result2 = solution.numTrees(n2)
print(result2)  # Output: 1

        
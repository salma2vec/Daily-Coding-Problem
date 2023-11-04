class Solution:
    """
    A class to decode a string containing only digits and count the number of ways to decode it.
    """

    def numDecodings(self, s: str) -> int:
        """
        Decode the given message and count the number of ways to decode it.

        Args:
            s (str): The input string to be decoded.

        Returns:
            int: The number of ways to decode the input string.
        """
        # Check for an empty string or if the first character is '0'
        if not s or s[0] == '0':
            return 0

        n = len(s)
        # Initialize a DP array to store the number of ways to decode
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: an empty string can be decoded in one way
        dp[1] = 1 if s[0] != '0' else 0  # Check the first character

        for i in range(2, n + 1):
            # Check if the current character can be used individually
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Check if the current and previous characters can be used together
            two_digits = int(s[i - 2:i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]

        return dp[n]

# Test the solution
solution = Solution()
s1 = "12"
print(solution.numDecodings(s1))  # Output: 2

s2 = "226"
print(solution.numDecodings(s2))  # Output: 3

s3 = "06"
print(solution.numDecodings(s3))  # Output: 0

        
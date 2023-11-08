class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n != len(s2):
            return False

        # Initialize a 3D DP array
        dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]

        # Base case: strings of length 1
        for i in range(n):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i][j][1] = True

        # Length of substring (size)
        for size in range(2, n + 1):
            for i in range(n - size + 1):
                for j in range(n - size + 1):
                    for k in range(1, size):
                        if (dp[i][j][k] and dp[i + k][j + k][size - k]) or (dp[i][j + size - k][k] and dp[i + k][j][size - k]):
                            dp[i][j][size] = True
                            break

        return dp[0][0][n]        
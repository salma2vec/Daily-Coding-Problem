INF = 1_000_000_000

class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for d in range(n):
            for idx in range(n):
                l, r = idx, idx + d
                if r >= n:
                    break
                dp[l][r] = INF
                if l == r:
                    dp[l][r] = 0
                elif s[l] != s[l + 1]:
                    dp[l][r] = min(dp[l][r], dp[l + 1][r] + 1)
                    for i in range(l + 1, r + 1):
                        if s[l] == s[i]:
                            dp[l][r] = min(dp[l][r], dp[l][i - 1] + dp[i][r])
                else:
                    dp[l][r] = dp[l + 1][r]

        return dp[0][n - 1] + 1
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (k + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            temp = [0] * (k + 1)
            temp[0] = 1
            for j in range(1, k + 1):
                temp[j] = (temp[j - 1] + dp[j]) % MOD
                if j >= i:
                    temp[j] = (temp[j] - dp[j - i] + MOD) % MOD
            dp = temp

        return dp[k]        
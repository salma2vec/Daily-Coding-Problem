class Solution(object):
    def waysToReachTarget(self, target, types):
        """
        :type target: int
        :type types: List[List[int]]
        :rtype: int
        """
        dp = [1] + [0] * target
        mod = 10 ** 9 + 7
        for c, m in types:
            for i in range(m, target + 1):
                dp[i] += dp[i - m]
            for i in range(target, (c + 1) * m - 1, -1):
                dp[i] = (dp[i] - dp[i - (c + 1) * m]) % mod
        return dp[-1] % mod        
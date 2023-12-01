class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:

        p = [0] + list(accumulate(nums))
        a = [(u, u + k - 1, (p[u + k] - p[u])) for u in range(0, len(nums) - k + 1)]

        n, d = len(a), 3

        dp = [[-inf for _ in range(d + 1)] for _ in range(n + 1)]
        for i in range(n + 1): dp[i][0] = 0

        h = defaultdict(list)
        for i in range(1, n + 1):
            for dd in range(1, d + 1):
                dp[i][dd] = max(dp[i][dd], dp[i - 1][dd])
                pv = (dp[i - k][dd - 1] if i - k >= 0 else 0)
                if dp[i][dd] < a[i - 1][2] + pv:
                    dp[i][dd] = a[i - 1][2] + pv
                    h[dp[i][dd]] = h[dp[i - k][dd - 1]] + [a[i - 1][0]]

        return h[dp[n][dd]]
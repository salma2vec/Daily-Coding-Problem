class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        @lru_cache(None)
        def dp(i, d):
            if i == len(rods): return 0 if d == 0 else -inf
            return max(dp(i + 1, d), rods[i] + dp(i + 1, d + rods[i]), dp(i + 1, d - rods[i]))
        return dp(0, 0)

        
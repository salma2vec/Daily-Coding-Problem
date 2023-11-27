class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [1] * 10
        moves = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        for _ in range(1, n):
            dp_next = [0] * 10
            for i in range(10):
                dp_next[i] = sum(dp[j] for j in moves[i]) % (10**9 + 7)
            dp = dp_next
        return sum(dp) % (10**9 + 7)

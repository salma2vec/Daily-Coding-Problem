class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        max_length = 1

        for num in arr:
            if num - difference in dp:
                dp[num] = dp[num - difference] + 1
                max_length = max(max_length, dp[num])
            else:
                dp[num] = 1

        return max_length
        
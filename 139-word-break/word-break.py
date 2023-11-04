class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)

        # initialize a boolean array to track if a substring can be segmented.
        dp = [False] * (n + 1)
        dp[0] = True  # an empty string can be segmented.

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]        
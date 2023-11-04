class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        dp = [[False] * n for _ in range(n)]

        start, max_len = 0, 1  

        # sll substrings of length 1 are palindromes.
        for i in range(n):
            dp[i][i] = True

        # check for palindromes of length 2.
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start, max_len = i, 2

        # check for palindromes of length 3 or more.
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1  # ending index of the current substring.
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    if length > max_len:
                        start, max_len = i, length

        return s[start:start + max_len]

        
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        is_palindrome = lambda x: x == x[::-1]
        n = len(s)
        return any(
            is_palindrome(s[:i]) and is_palindrome(s[i:j]) and is_palindrome(s[j:])
            for i in range(1, n - 1)
            for j in range(i + 1, n)
        )
        
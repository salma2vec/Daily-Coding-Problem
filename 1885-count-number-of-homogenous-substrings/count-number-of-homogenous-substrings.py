class Solution:
    def countHomogenous(self, s: str) -> int:
        
        MOD = 10**9 + 7
        n = len(s)
        ans = 0
        count = 1
        
        for i in range(1, n):
            if s[i] == s[i-1]:
                count += 1
            else:
                ans = (ans + (count * (count + 1) // 2)) % MOD
                count = 1
        
        ans = (ans + (count * (count + 1) // 2)) % MOD
        return ans

s = "abbcccaa"
solution = Solution()
result = solution.countHomogenous(s)
print(result)  # Output: 13
        
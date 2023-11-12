class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        total = k ** n
        seen = set()
        password = '0' * (n - 1)

        def dfs(node):
            nonlocal seen, password
            if len(seen) == total:
                return True
            for x in range(k):
                nei = node + str(x)
                if nei not in seen:
                    seen.add(nei)
                    password += str(x)
                    if dfs(nei[1:]):
                        return True
                    password = password[:-1]
                    seen.remove(nei)
            return False

        dfs(password)
        return password
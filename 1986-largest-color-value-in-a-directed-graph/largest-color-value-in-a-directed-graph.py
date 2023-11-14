from typing import List
from collections import defaultdict

class CycleDetectedException(Exception):
    pass

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        g = {}
        for i in range(n):
            g[i] = []
        for src, dst in edges:
            g[src].append(dst)

        path, visit = set(), set()
        dp = {i: defaultdict(int) for i in range(n)}

        def dfs(i):
            if i in path:
                raise CycleDetectedException

            if i in visit:
                return 0

            dp[i][colors[i]] = 1

            path.add(i)
            for nei in g[i]:
                dfs(nei)
                for c in dp[nei]:
                    neiCount = 1 + dp[nei][c] if c == colors[i] else dp[nei][c]
                    dp[i][c] = max(dp[i][c], neiCount)
            path.remove(i)
            visit.add(i)

        res = 0
        for i in range(len(colors)):
            try:
                dfs(i)
                res = max(res, max(dp[i].values()))
            except CycleDetectedException:
                return -1

        return res

solution = Solution()
colors = "rrrde"
edges = [[4, 2], [3, 4], [0, 3], [1, 0], [2, 1]]
print(solution.largestPathValue(colors, edges))  # Output: -1


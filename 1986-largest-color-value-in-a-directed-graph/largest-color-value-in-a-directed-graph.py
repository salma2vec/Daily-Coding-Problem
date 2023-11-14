class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)

        graph = defaultdict(list)
        in_degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1

        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)

        dp = [[0] * 26 for _ in range(n)]  # dp[i][c] stores the count of color 'c' in the longest path ending at node i
        result = 0

        while queue:
            node = queue.popleft()
            color = ord(colors[node]) - ord('a')
            dp[node][color] += 1
            result = max(result, dp[node][color])

            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                dp[neighbor] = [max(dp[neighbor][i], dp[node][i]) for i in range(26)]
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # checking if there is a cycle (some nodes are not processed)
        if sum(in_degree) > 0:
            return -1

        return result

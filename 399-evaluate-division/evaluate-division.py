class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}

        # Build the graph
        for (a, b), value in zip(equations, values):
            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}
            graph[a][b] = value
            graph[b][a] = 1 / value

        def dfs(start, end, visited):
            if start not in graph or end not in graph or start in visited:
                return -1

            if start == end:
                return 1

            visited.add(start)

            # Recursively calculate the product of edge values
            for neighbor, value in graph[start].items():
                result = dfs(neighbor, end, visited)
                if result != -1:
                    return value * result

            visited.remove(start)
            return -1

        results = []
        for query in queries:
            result = dfs(query[0], query[1], set())
            results.append(result if result != -1 else -1)

        return results        
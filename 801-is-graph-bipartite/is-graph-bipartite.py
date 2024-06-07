class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = {}  

        def dfs(node, color):
            # if the node is already colored check if it matches the expected color
            if node in colors:
                return colors[node] == color

            # assign the expected color to the node
            colors[node] = color

            # call DFS on all neighbors recursively alternating the color
            for neighbor in graph[node]:
                if not dfs(neighbor, 1 - color):
                    return False

            return True

        for node in range(n):
            if node not in colors:
                # if node is not colored,call DFS with an initial color of 0
                if not dfs(node, 0):
                    return False

        return True        
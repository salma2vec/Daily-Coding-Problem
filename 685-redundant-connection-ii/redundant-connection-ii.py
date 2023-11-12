class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def find(node):
            if parent[node] == 0:
                return node
            parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 == root2:
                return False
            parent[root1] = root2
            return True

        n = len(edges)
        parent = [0] * (n + 1)
        candidate1, candidate2 = None, None
        conflict_edge = None

        for edge in edges:
            u, v = edge
            if parent[v] == 0:
                parent[v] = u
            else:
                # If v already has a parent, it means there is a conflict
                # We store the current edge as a candidate for removal
                candidate1 = [parent[v], v]
                candidate2 = edge
                conflict_edge = edge

        # Reset parent array for cycle detection
        parent = [0] * (n + 1)

        for edge in edges:
            if edge == conflict_edge:
                continue
            if not union(edge[0], edge[1]):
                # If adding this edge creates a cycle, then the other candidate
                # is the answer (the one that causes the conflict)
                return candidate1 if candidate1 else edge

        # If no cycle is found, then the last added edge is the answer
        return conflict_edge 
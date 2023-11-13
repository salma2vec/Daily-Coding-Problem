from typing import Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None

        visited = {}  

        def dfs(original_node):
            if original_node in visited:
                return visited[original_node]

            clone_node = Node(original_node.val)
            visited[original_node] = clone_node

            for neighbor in original_node.neighbors:
                clone_node.neighbors.append(dfs(neighbor))

            return clone_node

        return dfs(node)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

solution = Solution()
cloned_node = solution.cloneGraph(node1)

        
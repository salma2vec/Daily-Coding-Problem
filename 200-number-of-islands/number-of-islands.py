class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == '0':
                return

            grid[row][col] = '0'  # Mark the current land cell as visited

            # Explore adjacent land cells in all four directions
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        m, n = len(grid), len(grid[0])
        num_islands = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    num_islands += 1
                    dfs(row, col)

        return num_islands
        
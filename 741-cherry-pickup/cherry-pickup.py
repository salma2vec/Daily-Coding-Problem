class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        memo = {}

        def dp(r1, c1, r2, c2):
            if (r1, c1, r2, c2) in memo:
                return memo[(r1, c1, r2, c2)]

            if (
                r1 >= rows or c1 >= cols or
                r2 >= rows or c2 >= cols or
                grid[r1][c1] == -1 or grid[r2][c2] == -1
            ):
                return float('-inf')

            if r1 == rows - 1 and c1 == cols - 1:
                return grid[r1][c1]
            elif r2 == rows - 1 and c2 == cols - 1:
                return grid[r2][c2]

            cherries = 0
            if r1 == r2 and c1 == c2:
                cherries += grid[r1][c1]
            else:
                cherries += grid[r1][c1] + grid[r2][c2]

            moves = [
                dp(r1, c1 + 1, r2, c2 + 1),
                dp(r1 + 1, c1, r2 + 1, c2),
                dp(r1, c1 + 1, r2 + 1, c2),
                dp(r1 + 1, c1, r2, c2 + 1)
            ]

            cherries += max(moves)

            memo[(r1, c1, r2, c2)] = cherries
            return cherries

        result = dp(0, 0, 0, 0)
        return max(result, 0)  # Ensure non-negative result

# Time Complexity: O(N^4)
# Space Complexity: O(N^2) 
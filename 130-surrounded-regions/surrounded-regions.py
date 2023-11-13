class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != 'O':
                return

            board[row][col] = '#'  # Mark the connected 'O' cell

            # Explore adjacent cells in all four directions
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        # Mark 'O' cells on the border and connected to them
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        # Flip the remaining 'O' cells to 'X' and revert marked cells back to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
        
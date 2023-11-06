class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_safe(row, col):
            # check if there is a queen in the same column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            # check upper left diagonal
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            
            # check upper right diagonal
            for i, j in zip(range(row, -1, -1), range(col, n)):
                if board[i][j] == 'Q':
                    return False
            
            return True
        
        def solve(row):
            if row == n:
                # found valid sol
                solutions.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = 'Q'
                    solve(row + 1)
                    board[row][col] = '.'
        
        solutions = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        solve(0)
        return len(solutions)        
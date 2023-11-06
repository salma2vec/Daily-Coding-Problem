class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Check if a word exists in the given grid.

        Args:
            board (List[List[str]]): The input grid of characters.
            word (str): The word to search for.

        Returns:
            bool: True if the word exists in the grid, False otherwise.
        """
        def dfs(i, j, k):
            if not (0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[k]):
                return False
            if k == len(word) - 1:
                return True
            tmp, board[i][j] = board[i][j], "/"
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = tmp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False        
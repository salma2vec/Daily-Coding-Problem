from typing import List

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        """
        Args:
            arr (List[int]): The input list of distinct integers.
            k (int): The number of consecutive rounds an integer needs to win.

        Returns:
            int: The integer which wins the game.
        """

        current_winner = arr[0]
        consecutive_wins = 0

        for i in range(1, len(arr)):
            if arr[i] > current_winner:
                current_winner = arr[i]
                consecutive_wins = 1
            else:
                consecutive_wins += 1

            if consecutive_wins == k:
                break

        return current_winner

        
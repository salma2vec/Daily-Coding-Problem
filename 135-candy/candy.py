from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        Calculate the minimum number of candies required to distribute to children.

        Args:
        ratings (List[int]): An array of ratings for each child.

        Returns:
        int: The minimum number of candies needed.
        """
        n = len(ratings)
        candies = [1] * n

        # Left to right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        total_candies = candies[n - 1]

        # Right to left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

            total_candies += candies[i]

        return total_candies

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        """
        Calculate the maximum number of monsters that can be eliminated before losing the game.

        Args:
            dist (List[int]): List of initial distances of monsters from the city.
            speed (List[int]): List of speeds of monsters in kilometers per minute.

        Returns:
            int: Maximum number of monsters that can be eliminated.
        """
        n = len(dist)
        arrival_times = [(dist[i] + speed[i] - 1) // speed[i] for i in range(n)]
        arrival_times.sort()

        for i in range(n):
            if arrival_times[i] <= i:
                return i  # You lose when a monster reaches the city at the same time the weapon is charged
        return n  # You can eliminate all monsters before they reach the city

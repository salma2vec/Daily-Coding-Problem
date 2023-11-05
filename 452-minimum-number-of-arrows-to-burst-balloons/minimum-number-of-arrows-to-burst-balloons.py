class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        Args:
            points (List[List[int]]): List of balloon intervals, each represented as [xstart, xend].

        Returns:
            int: Minimum number of arrows needed.

        Example:

        Input: points = [[10,16],[2,8],[1,6],[7,12]]
        Output: 2
        Explanation: The balloons can be burst by 2 arrows.
        """
        if not points:
            return 0

        # Sort the balloons by their ending points
        points.sort(key=lambda x: x[1])

        arrows = 1  # At least one arrow is needed
        end = points[0][1]

        for i in range(1, len(points)):
            if points[i][0] > end:
                arrows += 1
                end = points[i][1]

        return arrows

                
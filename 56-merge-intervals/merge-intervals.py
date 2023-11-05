from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge overlapping intervals and return non-overlapping intervals.

        Args:
            intervals (List[List[int]]): List of intervals where each interval is represented as [start, end].

        Returns:
            List[List[int]]: List of non-overlapping intervals.
        """
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])  # Sort by start values

        merged = [intervals[0]]

        for interval in intervals[1:]:
            curr_start, curr_end = interval
            last_start, last_end = merged[-1]

            if curr_start <= last_end:
                # Merge the current interval with the last one
                merged[-1] = [last_start, max(last_end, curr_end)]
            else:
                # Add the current interval as a new non-overlapping interval
                merged.append(interval)

        return merged

                
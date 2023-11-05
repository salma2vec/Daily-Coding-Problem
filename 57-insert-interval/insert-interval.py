class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Args:
            intervals (List[List[int]]): List of non-overlapping intervals sorted
            newInterval (List[int]): Interval to insert into the list.

        Returns:
            List[List[int]]: List of intervals after the insertion.

        Example:
        Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
        Output: [[1,5],[6,9]]
        """
        result = []
        i = 0
        n = len(intervals)
        
        # Add all intervals that come before the newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        result.append(newInterval)
        
        # Add the remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result

                
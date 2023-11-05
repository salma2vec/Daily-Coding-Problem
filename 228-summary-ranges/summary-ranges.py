from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        Args:
            nums (List[int]): A sorted unique integer array.

        Returns:
            List[str]: List of ranges in string format.

        Example:

        Input: nums = [0,1,2,4,5,7]
        Output: ["0->2","4->5","7"]
        Explanation: The ranges are:
        [0,2] --> "0->2"
        [4,5] --> "4->5"
        [7,7] --> "7"
        """
        if not nums:
            return []

        ranges = []
        start, end = nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{end}")
                start, end = nums[i], nums[i]

        if start == end:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}->{end}")

        return ranges

        
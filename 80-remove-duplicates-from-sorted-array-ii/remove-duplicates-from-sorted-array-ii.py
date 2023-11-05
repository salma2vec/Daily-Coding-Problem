from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Args:
            nums (List[int]): The sorted array with duplicates.

        Returns:
            int: The number of unique elements after modification.
        """
        if not nums:
            return 0

        k = 2  # Initialize count of unique elements with an allowance of at most 2 occurrences
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k

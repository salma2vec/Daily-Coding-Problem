from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Find the majority element in the given list 'nums'.

        Args:
            nums (List[int]): The list of integers.

        Returns:
            int: The majority element.
        """
        candidate, count = nums[0], 1

        for i in range(1, len(nums)):
            if count == 0:
                candidate = nums[i]
                count = 1
            elif candidate == nums[i]:
                count += 1
            else:
                count -= 1

        return candidate

        
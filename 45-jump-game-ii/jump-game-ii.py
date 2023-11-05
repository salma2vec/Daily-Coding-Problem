from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Calculate the minimum number of jumps required to reach the last index in the array 'nums'.

        Args:
            nums (List[int]): The list of integers representing maximum jump lengths.

        Returns:
            int: The minimum number of jumps required.
        """
        if len(nums) == 1:
            return 0  # If there's only one element, no jumps needed

        jumps = 0  # Initialize the number of jumps
        farthest = 0  # Initialize the farthest position you can reach
        currentEnd = 0  # Initialize the current end index

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])  # Update the farthest position

            if i == currentEnd:
                jumps += 1  # Increment the number of jumps
                currentEnd = farthest

        return jumps

        
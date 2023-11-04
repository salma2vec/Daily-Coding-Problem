from typing import List

class Solution:
    """
    A class to find the number of possible combinations that add up to a target integer.
    """

    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        Calculate the number of possible combinations to add up to the target using the provided integers.

        Args:
            nums (List[int]): A list of distinct integers.
            target (int): The target integer.

        Returns:
            int: The number of possible combinations to add up to the target.
        """
        # Create a list to store the number of combinations for each target value from 0 to the target
        dp = [0] * (target + 1)

        # Initialize the number of combinations for target 0 as 1
        dp[0] = 1

        # Iterate through each possible target value
        for i in range(1, target + 1):
            # For each target value, iterate through the given integers
            for num in nums:
                # Update the number of combinations for the current target value
                if i >= num:
                    dp[i] += dp[i - num]

        return dp[target]

# Test the solution
solution = Solution()
nums1 = [1, 2, 3]
target1 = 4
print(solution.combinationSum4(nums1, target1))  # Output: 7

nums2 = [9]
target2 = 3
print(solution.combinationSum4(nums2, target2))  # Output: 0

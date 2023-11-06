from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Generate all possible combinations of k numbers chosen from the range [1, n].

        Args:
            n (int): The range of numbers from 1 to n.
            k (int): The number of elements in each combination.

        Returns:
            List[List[int]]: A list of all possible combinations.
        """
        def backtrack(start, current_combination):
            if len(current_combination) == k:
                result.append(current_combination[:])
                return

            for i in range(start, n + 1):
                current_combination.append(i)
                backtrack(i + 1, current_combination)
                current_combination.pop()

        result = []
        backtrack(1, [])
        return result



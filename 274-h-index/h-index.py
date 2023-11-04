from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        Calculate the researcher's h-index.

        Args:
        citations (List[int]): A list of citations for each paper.

        Returns:
        int: The h-index of the researcher.
        """
        citations.sort(reverse=True)
        h_index = 0
        
        for i, citation in enumerate(citations):
            if i + 1 <= citation:
                h_index = i + 1
            else:
                break
        
        return h_index

solution = Solution()
citations1 = [3, 0, 6, 1, 5]
result1 = solution.hIndex(citations1)
print(f"Example 1 Output: {result1}")

citations2 = [1, 3, 1]
result2 = solution.hIndex(citations2)
print(f"Example 2 Output: {result2}")

        
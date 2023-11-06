class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Find all unique combinations of candidates where the chosen numbers sum to the target.

        Args:
            candidates (List[int]): A list of distinct integers.
            target (int): The target sum.

        Returns:
            List[List[int]]: A list of all unique combinations.
        """
        def backtrack(remaining, current_combination, start):
            if remaining == 0:
                result.append(current_combination[:])
                return
            if remaining < 0:
                return
            for i in range(start, len(candidates)):
                current_combination.append(candidates[i])
                backtrack(remaining - candidates[i], current_combination, i)
                current_combination.pop()

        result = []
        backtrack(target, [], 0)
        return result        
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible permutations of distinct integers in the `nums` array.

        Args:
            nums (List[int]): A list of distinct integers.

        Returns:
            List[List[int]]: A list of all possible permutations.
        """
        def backtrack(first):
            if first == n:
                result.append(nums[:])
                return

            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        result = []
        backtrack(0)
        return result

        
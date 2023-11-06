from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Generates all possible letter combinations for the given phone digits.

        Args:
            digits (str): A string containing digits from 2-9 inclusive.

        Returns:
            List[str]: A list of all possible letter combinations.
        """
        if not digits:
            return []

        # Define a dictionary to map digits to corresponding letters
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(index, current_combination):
            if index == len(digits):
                result.append(current_combination)
                return

            current_digit = digits[index]
            letters = digit_to_letters[current_digit]

            for letter in letters:
                backtrack(index + 1, current_combination + letter)

        result = []
        backtrack(0, '')
        return result


# solution = Solution()
# combinations = solution.letterCombinations("23")
# print(combinations)

        
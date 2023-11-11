class Solution:
    def numSplits(self, s: str) -> int:
        char_freq = {}
        left_chars = set()
        good_splits = 0

        # Initialize frequency map
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1

        # Add each char to the left substring and check for good splits
        for current_char in s:
            left_chars.add(current_char)
            char_freq[current_char] -= 1

            if char_freq[current_char] == 0:
                char_freq.pop(current_char)

            if len(char_freq.keys()) == len(left_chars):
                good_splits += 1

        return good_splits
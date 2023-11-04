class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_count_t = {}
        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1

        left, right, min_len = 0, 0, float('inf')
        min_len_start = 0
        chars_to_match = len(char_count_t)

        while right < len(s):
            if s[right] in char_count_t:
                char_count_t[s[right]] -= 1
                if char_count_t[s[right]] == 0:
                    chars_to_match -= 1

            while chars_to_match == 0:
                if right - left < min_len:
                    min_len = right - left
                    min_len_start = left

                if s[left] in char_count_t:
                    char_count_t[s[left]] += 1
                    if char_count_t[s[left]] > 0:
                        chars_to_match += 1

                left += 1

            right += 1

        return "" if min_len == float('inf') else s[min_len_start:min_len_start + min_len + 1]
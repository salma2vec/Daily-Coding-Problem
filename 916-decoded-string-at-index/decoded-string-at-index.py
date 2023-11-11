class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0

        for char in s:
            if char.isalpha():
                length += 1
            elif char.isdigit():
                repeat_count = int(char)
                length *= repeat_count

        for char in reversed(s):
            k %= length
            if k == 0 and char.isalpha():
                return char

            if char.isalpha():
                length -= 1
            elif char.isdigit():
                repeat_count = int(char)
                length //= repeat_count        
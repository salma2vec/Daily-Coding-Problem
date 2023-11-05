from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result, line, line_length = [], [], 0

        for word in words:
            if line_length + len(line) + len(word) <= maxWidth:
                line.append(word)
                line_length += len(word)
            else:
                extra_spaces = maxWidth - line_length
                space_count = len(line) - 1 if len(line) > 1 else 1
                spaces_between, extra_spaces = divmod(extra_spaces, space_count)
                line_str = line[0]

                for i in range(1, len(line)):
                    spaces = ' ' * spaces_between
                    if i <= extra_spaces:
                        spaces += ' '
                    line_str += spaces + line[i]

                result.append(line_str.ljust(maxWidth))

                line, line_length = [word], len(word)

        result.append(' '.join(line).ljust(maxWidth))
        return result

class Solution:
    def calculate(self, s: str) -> int:
        """
        Evaluate a basic mathematical expression represented as a string.

        Args:
            s (str): The input expression as a string.

        Returns:
            int: The result of the evaluation.
        """
        def evaluate(tokens):
            stack = []
            num = 0
            sign = 1

            for token in tokens:
                if token == "+":
                    sign = 1
                elif token == "-":
                    sign = -1
                elif token == "(":
                    stack.append((num, sign))
                    num = 0
                    sign = 1
                elif token == ")":
                    prev_num, prev_sign = stack.pop()
                    num = prev_num + prev_sign * num
                else:
                    num += sign * int(token)

            return num

        tokens = []
        i = 0

        while i < len(s):
            if s[i].isdigit():
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                tokens.append(s[i:j])
                i = j
            elif s[i] in "+-()":
                tokens.append(s[i])
                i += 1
            else:
                i += 1

        return evaluate(tokens)        
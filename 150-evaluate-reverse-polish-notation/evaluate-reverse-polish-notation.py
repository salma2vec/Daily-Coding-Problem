from typing import List

class Solution:
    @classmethod
    def evalRPN(cls, tokens: List[str]) -> int:
        """
        Evaluate a Reverse Polish Notation (RPN) expression.

        Args:
            tokens (List[str]): List of tokens representing an RPN expression.

        Returns:
            int: The result of evaluating the RPN expression.
        """
        stack = []
        operators = set(['+', '-', '*', '/'])

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
        
        return stack[0]


tokens1 = ["2", "1", "+", "3", "*"]
print(Solution.evalRPN(tokens1))  # Output: 9

tokens2 = ["4", "13", "5", "/", "+"]
print(Solution.evalRPN(tokens2))  # Output: 6

tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(Solution.evalRPN(tokens3))  # Output: 22

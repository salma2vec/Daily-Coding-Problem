class MinStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []  # Main stack to store elements
        self.min_stack = []  # Auxiliary stack to store minimum values

    def push(self, val: int) -> None:
        """
        Push element onto the stack.
        """
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        """
        Remove the element on the top of the stack.
        """
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        """
        Get the top element of the stack.
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        """
        Retrieve the minimum element in the stack.
        """
        if self.min_stack:
            return self.min_stack[-1]

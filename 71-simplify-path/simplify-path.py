class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Simplify the given absolute path to its canonical form.

        Args:
            path (str): Absolute path string.

        Returns:
            str: Simplified canonical path.

        Example:

        Input: path = "/home//foo/"
        Output: "/home/foo"
        """
        components = path.split('/')
        stack = []

        for component in components:
            if component == '' or component == '.':
                continue
            elif component == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(component)

        return '/' + '/'.join(stack)        
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Class to solve the problem of calculating the total sum of all root-to-leaf numbers.
    """
    def sumNumbers(self, root: TreeNode) -> int:
        """
        Calculate the total sum of all root-to-leaf numbers.
        
        Args:
            root (TreeNode): The root of the binary tree.
        
        Returns:
            int: The total sum of all root-to-leaf numbers.
        """
        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum = current_sum * 10 + node.val

            if not node.left and not node.right:
                return current_sum

            left_sum = dfs(node.left, current_sum)
            right_sum = dfs(node.right, current_sum)

            return left_sum + right_sum

        return dfs(root, 0)

        
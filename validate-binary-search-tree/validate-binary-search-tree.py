# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Determine if the binary tree is a valid Binary Search Tree (BST).

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            bool: True if the tree is a valid BST, False otherwise.
        """
        def is_valid(node, lower, upper):
            if not node:
                return True
            if not lower < node.val < upper:
                return False
            return is_valid(node.left, lower, node.val) and is_valid(node.right, node.val, upper)

        return is_valid(root, float('-inf'), float('inf'))        
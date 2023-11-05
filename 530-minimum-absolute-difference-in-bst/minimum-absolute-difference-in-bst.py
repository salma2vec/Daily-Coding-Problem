# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        Find the minimum absolute difference between the values of any two different nodes in the BST.

        Args:
            root (Optional[TreeNode]): The root of the Binary Search Tree.

        Returns:
            int: The minimum absolute difference.
        """
        def inorder(node):
            nonlocal prev, min_diff
            if not node:
                return
            inorder(node.left)
            if prev is not None:
                min_diff = min(min_diff, abs(node.val - prev))
            prev = node.val
            inorder(node.right)

        prev = None
        min_diff = float('inf')
        inorder(root)
        return min_diff        
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root, k):
        """
        Find the kth smallest value in a binary search tree.
        
        Args:
            root (TreeNode): The root of the binary search tree.
            k (int): The kth value to find (1-indexed).

        Returns:
            int: The kth smallest value.
        """
        def inOrderTraversal(node):
            nonlocal k, result
            if not node:
                return

            # Traverse the left subtree
            inOrderTraversal(node.left)

            # Visit the current node
            k -= 1
            if k == 0:
                result = node.val
                return

            # Traverse the right subtree
            inOrderTraversal(node.right)

        result = None
        inOrderTraversal(root)
        return result

        
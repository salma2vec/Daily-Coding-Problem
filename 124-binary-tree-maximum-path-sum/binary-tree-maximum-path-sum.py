class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        """
        Return the maximum path sum of any non-empty path in the binary tree.

        :param root: Root of the binary tree.
        :type root: TreeNode
        :return: Maximum path sum.
        :rtype: int
        """
        def max_path_sum_helper(node):
            nonlocal max_sum
            if not node:
                return 0
            
            # Calculate the maximum path sum for the left and right subtrees
            left_sum = max(0, max_path_sum_helper(node.left))
            right_sum = max(0, max_path_sum_helper(node.right))
            
            # Update the global maximum path sum
            max_sum = max(max_sum, node.val + left_sum + right_sum)
            
            # Return the maximum path sum that can include the current node
            return node.val + max(left_sum, right_sum)
        
        max_sum = float('-inf')
        max_path_sum_helper(root)
        return max_sum

# Example usage:
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(-10)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(7)

solution = Solution()
result1 = solution.maxPathSum(root1)  # Output: 6
result2 = solution.maxPathSum(root2)  # Output: 42
print(result1)
print(result2)

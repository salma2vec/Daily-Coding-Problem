class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root):
        """
        Return the maximum amount of money the thief can rob without alerting the police.

        :param root: Root of the binary tree.
        :type root: TreeNode
        :return: Maximum amount of money that can be robbed.
        :rtype: int
        """
        def rob_helper(node):
            if not node:
                return (0, 0)
            
            # Recursively calculate the values for the left and right subtrees
            left_rob, left_not_rob = rob_helper(node.left)
            right_rob, right_not_rob = rob_helper(node.right)
            
            # Calculate the maximum amount of money for the current node
            rob_this_node = node.val + left_not_rob + right_not_rob
            not_rob_this_node = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
            
            return (rob_this_node, not_rob_this_node)
        
        rob_amount, not_rob_amount = rob_helper(root)
        return max(rob_amount, not_rob_amount)

# Example usage:
root1 = TreeNode(3)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(3)
root1.right.right = TreeNode(1)

root2 = TreeNode(3)
root2.left = TreeNode(4)
root2.right = TreeNode(5)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(3)
root2.right.right = TreeNode(1)

solution = Solution()
result1 = solution.rob(root1)  # Output: 7
result2 = solution.rob(root2)  # Output: 9
print(result1)
print(result2)

        
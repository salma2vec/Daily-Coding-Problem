class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n):
        """
        Generate all structurally unique BSTs with n nodes.

        :param n: Number of nodes.
        :type n: int
        :return: List of TreeNode representing all unique BSTs.
        :rtype: List[TreeNode]
        """
        def generate_trees(start, end):
            if start > end:
                return [None]
            
            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate_trees(start, i - 1)
                right_trees = generate_trees(i + 1, end)
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
            return all_trees
        
        if n == 0:
            return []
        
        return generate_trees(1, n)

# Example usage:
n1 = 3
solution = Solution()
result1 = solution.generateTrees(n1)
for tree in result1:
    print(tree)  # Output: List representation of unique BSTs

n2 = 1
result2 = solution.generateTrees(n2)
for tree in result2:
    print(tree)  # Output: List representation of unique BSTs

        
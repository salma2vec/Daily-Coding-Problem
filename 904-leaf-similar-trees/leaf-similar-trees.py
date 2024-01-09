# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root.left:
                yield from dfs(root.left)
            if root.right:
                yield from dfs(root.right)
            if not root.left and not root.right:
                yield root.val

        iter1 = dfs(root1)
        iter2 = dfs(root2)
        for i,j in zip_longest(iter1,iter2,fillvalue=None):
            if i!=j:
                return False

        return True
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        mini = float("inf")
        def dfs(curr = root, level = 0):
            nonlocal mini
            if curr:
                if curr.left==None and curr.right==None:
                    mini = min(mini, level)
                else:
                    dfs(curr.left, level + 1)
                    dfs(curr.right, level + 1)
            return
        dfs()
        return mini+1        
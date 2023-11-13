# Definition for a binary tree node.
class Solution:
    def __init__(self, val=0, left=None, right=None):
        self.prev = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.right)  
        self.flatten(root.left) 
        root.right = self.prev  
        root.left = None  
        self.prev = root  
        
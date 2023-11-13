# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if the root is None or matches either p or q, return the root
        if not root or root == p or root == q:
            return root
        
        # Recursively search for the LCA in the left and right subtrees
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right subtrees have an LCA, then the current root is the LCA
        if left_lca and right_lca:
            return root
        
        # If only one subtree has an LCA, return that LCA
        return left_lca if left_lca else right_lca






        
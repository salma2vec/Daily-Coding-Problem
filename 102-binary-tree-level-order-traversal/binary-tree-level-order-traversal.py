# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root, None])  # Use None as a level separator

        current_level = []
        while queue:
            node = queue.popleft()

            if node is None:
                # End of the current level
                result.append(current_level)
                current_level = []

                if queue:
                    queue.append(None)  # Add level separator for the next level
            else:
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result        
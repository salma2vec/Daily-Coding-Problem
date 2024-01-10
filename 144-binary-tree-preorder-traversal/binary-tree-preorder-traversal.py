# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preOrder(self,root,answerList):
        if root == None:
            return answerList
        else:
            answerList.append(root.val)
            self.preOrder(root.left, answerList)
            self.preOrder(root.right, answerList)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answerList = []
        self.preOrder(root, answerList)

        return answerList        
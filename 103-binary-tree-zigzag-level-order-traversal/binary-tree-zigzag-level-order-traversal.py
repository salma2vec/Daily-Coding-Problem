# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lvls = defaultdict(list)
        q = []
        q.append((root,0))
        while len(q)>0:
            cur_n, cur_lvl = q.pop(0)
            if cur_n != None:
                lvls[cur_lvl].append(cur_n.val)
                q.append((cur_n.left, cur_lvl+1))
                q.append((cur_n.right, cur_lvl+1))
        
        ans = []
        for lvl in lvls:
            if lvl%2==0:
                ans.append(lvls[lvl])
            else:
                ans.append(lvls[lvl][::-1])
        
        return ans
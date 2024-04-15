/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public int SumNumbers(TreeNode root) {
        return SumNumbers(root, 0);

        int SumNumbers(TreeNode node, int s) {
            if (node == null) return 0;

            s = (s * 10) + node.val;

            if (node.left == null && node.right ==null) return s;

            return SumNumbers(node.left, s) + SumNumbers(node.right, s);
        }
    }
}

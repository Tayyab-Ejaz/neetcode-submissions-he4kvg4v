# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def helper(self, root: Optional[TreeNode]) -> int:
        if(not root):
            return 0;
        leftHeight = self.helper(root.left);
        rightHeight = self.helper(root.right);
        maxDecendentHeight = max(leftHeight, rightHeight);
        return maxDecendentHeight + 1;

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root);
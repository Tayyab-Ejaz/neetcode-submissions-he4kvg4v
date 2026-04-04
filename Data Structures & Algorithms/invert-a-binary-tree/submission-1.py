# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
    if(not node):
        
        return;
    node.left, node.right = node.right,node.left
    if(node.left):
        dfs(node.left);

    if(node.right):
        dfs(node.right);

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dfs(root);

        return root

        
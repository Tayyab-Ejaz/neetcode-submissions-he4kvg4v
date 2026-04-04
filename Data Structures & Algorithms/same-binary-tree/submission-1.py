# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         tree1_tace = []
#         tree2_tace = []
#         def dfs_trace(node, trace):
#             if not node:
#                 trace.append(None)
#                 return trace;

#             dfs_trace(node.left, trace);
#             dfs_trace(node.right, trace);
#             trace.append(node.val)
#         dfs_trace(p, tree1_tace)
#         dfs_trace(q, tree2_tace)

#         return tree1_tace == tree2_tace


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False





            
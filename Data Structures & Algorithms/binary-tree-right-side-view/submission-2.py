# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#         rightSideView = []
#         level = [root]
#         while(level):
#             rightSideView.append(level[-1].val)
#             newLevel= []
#             for x in level:
#                 if(x.left):
#                     newLevel.append(x.left)

#                 if(x.right):
#                     newLevel.append(x.right)
#             level = newLevel

#         return rightSideView


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []

        def dfs(root, depth):
            if not root:
                return None;
            if(depth == len(result)):
                result.append(root.val)
            dfs(root.right, depth+1)
            dfs(root.left, depth+1)

        dfs(root, 0)
        return result;
        
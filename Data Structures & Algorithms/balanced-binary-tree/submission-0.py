# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    allSubtreeBalanced = True;
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if(not node):
                return 0;
            leftHeight = height(node.left);
            rightHeight = height(node.right);
            print("node: ", node.val, "leftHeight: ", leftHeight, "rightHeight: ", rightHeight )
            if(self.allSubtreeBalanced):
                self.allSubtreeBalanced = abs(rightHeight - leftHeight) <= 1 
            return max(leftHeight, rightHeight) + 1
        height(root);
        return self.allSubtreeBalanced;
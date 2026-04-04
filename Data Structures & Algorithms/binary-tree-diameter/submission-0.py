class Solution:
    maxD = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.maxD = max(self.maxD, left + right)
            return 1 + max(left, right)
        
        depth(root)
        return self.maxD
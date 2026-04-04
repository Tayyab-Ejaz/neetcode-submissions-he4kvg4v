class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate_tree(node, min_val, max_val):
            if not node:
                return True;
            
            if not (min_val < node.val < max_val):
                return False

            left_response = validate_tree(node.left, min_val, node.val);
            right_response = validate_tree(node.right, node.val, max_val);
            
            return left_response and right_response
            
        return validate_tree(root, float('-inf'), float('inf'))
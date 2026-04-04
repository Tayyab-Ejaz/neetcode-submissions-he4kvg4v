# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return []
        nested_list = []
        bfs_queue = [root]
        while(bfs_queue):
            sub_list = []
            new_bfs_queue = []
            for n in bfs_queue:
                sub_list.append(n.val);

                if(n.left):
                    new_bfs_queue.append(n.left)
                if(n.right):
                    new_bfs_queue.append(n.right)

            nested_list.append(sub_list);
            
                            
            bfs_queue = list(new_bfs_queue);
        return nested_list

        
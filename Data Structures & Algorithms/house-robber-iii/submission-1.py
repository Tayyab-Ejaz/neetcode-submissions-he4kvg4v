
class Solution:
    def __init__(self):
        self.cache = {}
    def dfs(self, root):
        if not root:
            return 0
        if root in self.cache:
            return self.cache[root]
        
        benefitOfCurrent = root.val
        if(root.left):
            benefitOfCurrent += self.dfs(root.left.left)
            benefitOfCurrent += self.dfs(root.left.right)

        if(root.right):
            benefitOfCurrent += self.dfs(root.right.left)
            benefitOfCurrent += self.dfs(root.right.right)
        res = max([benefitOfCurrent, self.dfs(root.left) + self.dfs(root.right)])
        self.cache[root] = res
        return res
    def rob(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
        
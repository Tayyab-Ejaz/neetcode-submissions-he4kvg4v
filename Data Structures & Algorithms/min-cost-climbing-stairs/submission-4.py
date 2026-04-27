class Solution:
    def dfs(self, costs, current_idx, memo):
        if(current_idx >= len(costs)):
            return 0

        if(current_idx in memo):
            return memo[current_idx]

        option1 = self.dfs(costs, current_idx + 1, memo)
        option2 = self.dfs(costs, current_idx + 2, memo)

        memo[current_idx] = min(option1, option2) + costs[current_idx]
        return min(option1, option2) + costs[current_idx]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        return min(self.dfs(cost, 0, memo), self.dfs(cost, 1, memo))

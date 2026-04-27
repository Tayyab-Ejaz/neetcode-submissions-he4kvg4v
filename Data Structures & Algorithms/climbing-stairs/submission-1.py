class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        if(n <= 1):
            return 1;

        if(n in self.memo):
            return self.memo[n]

        leftOptions = 0        
        leftOptions = self.climbStairs(n-2)

        rightOptions = self.climbStairs(n-1)  

        self.memo[n] = leftOptions + rightOptions
        return leftOptions + rightOptions
        


        
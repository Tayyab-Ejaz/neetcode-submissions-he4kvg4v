class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        if(n == 0):
            return 1;

        if(n in self.memo):
            return self.memo[n]

        leftOptions = 0        
        if(n > 1):
            leftOptions = self.climbStairs(n-2)

        rightOptions = self.climbStairs(n-1)  

        self.memo[n] = leftOptions + rightOptions
        return leftOptions + rightOptions
        


        
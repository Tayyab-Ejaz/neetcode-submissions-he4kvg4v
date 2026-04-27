class Solution:
    memo = {}
    def numberOfOnes(self, n):
        ones = 0
        while(n != 0):
            if(n in self.memo):
                ones += self.memo[n]
                break
            n = n & (n-1) # Bit manipulation. n and (n-1), removes the right most 1 from n
            ones += 1
        self.memo[n] = ones
        return self.memo[n]

    def countBits(self, n: int) -> List[int]:
        result = [self.numberOfOnes(i) for i in range(0, n + 1)]
        return result

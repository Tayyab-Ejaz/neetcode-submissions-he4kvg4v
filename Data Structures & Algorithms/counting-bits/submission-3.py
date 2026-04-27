class Solution:
    def numberOfOnes(self, n):
        ones = 0

        while(n != 0):
            n = n & (n-1)
            ones += 1
       
        return ones

    def countBits(self, n: int) -> List[int]:
        result = [self.numberOfOnes(i) for i in range(0, n + 1)]
        return result

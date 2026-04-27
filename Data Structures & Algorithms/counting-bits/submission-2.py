class Solution:
    def __init__(self):
        self.memo = {}

    def numberOfOnes(self, n):
        original = n
        ones = 0

        while n > 0:
            if n in self.memo:
                ones += self.memo[n]
                break

            ones += n % 2
            n //= 2

        self.memo[original] = ones
        return ones

    def countBits(self, n: int):
        return [self.numberOfOnes(i) for i in range(n + 1)]
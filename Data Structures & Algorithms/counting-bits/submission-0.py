class Solution:
    def numberOfOnes(self, n):
        ones = 0

        while n // 2 > 0:
            remainder = n % 2
            if remainder > 0:
                ones += 1

            n = n // 2

        if n > 0:
            ones += 1
        return ones

    def countBits(self, n: int) -> List[int]:
        result = [self.numberOfOnes(i) for i in range(0, n + 1)]
        return result

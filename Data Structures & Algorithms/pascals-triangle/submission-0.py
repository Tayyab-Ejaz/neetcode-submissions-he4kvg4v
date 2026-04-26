class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalTriangle = []

        for i in range(numRows):
            row = []

            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(
                        pascalTriangle[i - 1][j - 1] + pascalTriangle[i - 1][j]
                    )

            pascalTriangle.append(row)

        return pascalTriangle
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascalTriangle = []

        rowIndex += 1
        for i in range(rowIndex):
            row = []

            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(
                        pascalTriangle[i - 1][j - 1] + pascalTriangle[i - 1][j]
                    )

            pascalTriangle.append(row)
        return pascalTriangle[rowIndex-1]
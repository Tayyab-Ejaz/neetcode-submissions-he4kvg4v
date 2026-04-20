class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        rows = len(matrix)
        columns = len(matrix[0])
        j =  rows * columns - 1

        while(i <= j):
            mid = (j + i) // 2
            m = mid // columns
            n = mid % columns
            if(matrix[m][n] == target):
                return True;
            elif(matrix[m][n] < target):
                i = mid + 1
            elif (matrix[m][n] > target):
                j = mid - 1
        return False

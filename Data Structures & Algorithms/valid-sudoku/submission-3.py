class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            dots = Counter(row).get('.', 0)
            if (len(set(row)) + dots - 1) != len(row):
                return False
        print("executed rows")
        for j in range(0, 9):
            col = []
            for i in range(0, len(board)):
                col.append(board[i][j])

            dots = Counter(col).get('.', 0)
            if (len(set(col)) + dots - 1) != len(col):
                print(f"{col}, {len(set(col))}, {len(set(col)) + dots - 1}, {dots}")
                return False
        print("executed cols")
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                matrix = []
                for k in range(0, 3):
                    for l in range(0, 3):
                        matrix.append(board[i + k][j + l])
                dots = Counter(matrix).get('.', 0)
                if (len(set(matrix)) + dots - 1) != len(matrix):
                    return False

        print("executed grids")
        
        return True
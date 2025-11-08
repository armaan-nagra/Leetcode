class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        copy_matrix = []
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(matrix[r][c])
            copy_matrix.append(row)
        print(copy_matrix)

        
        def zero_row(row):
            for c in range(cols):
                matrix[row][c] = 0
        
        def zero_col(col):
            for r in range(rows):
                matrix[r][col] = 0
                
        for r in range(rows):
            for c in range(cols):
                if copy_matrix[r][c] == 0:
                    zero_row(r)
                    zero_col(c)
        

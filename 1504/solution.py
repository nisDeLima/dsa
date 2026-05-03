class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])

        for row in range(ROWS):
            for col in range(COLS - 2, -1, -1):
                if mat[row][col] == 1:
                    mat[row][col] += mat[row][col + 1]
        
        res = 0

        for row in range(ROWS):
            for col in range(COLS): 
                if mat[row][col] == 0:
                    continue
                min_width = mat[row][col]
                for aux_row in range(row, ROWS):
                    min_width = min(mat[aux_row][col], min_width)
                    res += min_width

        return res

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        for row in range(1, ROWS):
            for col in range(COLS):
                if matrix[row][col] == 1:
                    matrix[row][col] += matrix[row - 1][col]

        res = 0
        for row in range(ROWS):
            sorted_row = sorted(matrix[row], reverse=True)
            for col in range(COLS):
                res = max(res, sorted_row[col] * (col + 1))

        return res

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sum_mat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        # Process prefix sum
        for row in range(ROWS):
            prefix = 0
            for col in range(COLS):
                prefix += matrix[row][col]
                above = self.sum_mat[row][col + 1]
                self.sum_mat[row + 1][col + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        total = self.sum_mat[row2][col2]
        above = self.sum_mat[row1 - 1][col2]
        left = self.sum_mat[row2][col1 - 1]
        top_left = self.sum_mat[row1 - 1][col1 - 1]

        return total - above - left + top_left



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

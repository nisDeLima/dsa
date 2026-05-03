class Solution:
    def countSquares_removed(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}

        def dfs(row, col):
            if(
                row >= ROWS or row < 0 or
                col >= COLS or col < 0 or
                matrix[row][col] == 0
            ):
                return 0
            if (row, col) in cache:
                return cache[(row, col)]

            num_squares = 1 + min(
                dfs(row + 1, col + 1),
                dfs(row + 1, col),
                dfs(row, col + 1),
            )

            cache[(row, col)] = num_squares
            return cache[(row,col)]
        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                res += dfs(row, col)
        return res
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        prev_row = matrix[ROWS - 1]
        prev_row.append(0)

        res = sum(prev_row)

        for row in range(ROWS - 2, -1, -1):
            curr_row = [0] * (COLS + 1)
            for col in range(COLS - 1, -1, -1):
                if matrix[row][col] == 1:
                    curr_row[col] = 1 + min(curr_row[col + 1], prev_row[col], prev_row[col + 1])
                    res += curr_row[col]
            prev_row = curr_row

        return res



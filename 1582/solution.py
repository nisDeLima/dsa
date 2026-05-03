class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])
        rows_sum = defaultdict(int)
        cols_sum = defaultdict(int)
        one_positions = set()

        for row in range(ROWS):
            for col in range(COLS):
                val = mat[row][col]
                if val == 1:
                    one_positions.add((row, col))
                rows_sum[row] += val
                cols_sum[col] += val
        
        res = 0

        for row, col in one_positions:
            if rows_sum[row] == cols_sum[col] == 1:
                res += 1
        
        return res


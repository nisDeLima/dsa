class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        MOD = 10 ** 9 + 7

        @cache
        def dp(row, col):
            if row == ROWS - 1 and col == COLS - 1:
                val = grid[row][col]
                return val, val

            curr = grid[row][col]
            neighbors = []
            if col + 1 < COLS:
                neighbors.append(dp(row, col + 1))
            if row + 1 < ROWS:
                neighbors.append(dp(row + 1, col))

            products = [curr * val for mx, mn in neighbors for val in (mx, mn)]
            return max(products), min(products)

        result = dp(0, 0)[0]
        return result % MOD if result >= 0 else -1

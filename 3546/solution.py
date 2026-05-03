class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        total = 0

        row_sums = [0] * ROWS
        col_sums = [0] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                row_sums[r] += grid[r][c]
                col_sums[c] += grid[r][c]
                total += grid[r][c]

        # horizontal cut: split between row i and row i+1
        running = 0
        for i in range(ROWS - 1):
            running += row_sums[i]
            if running == total - running:
                return True

        # vertical cut: split between col i and col i+1
        running = 0
        for i in range(COLS - 1):
            running += col_sums[i]
            if running == total - running:
                return True

        return False

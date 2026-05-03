class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                curr = grid[row][col]
                left = grid[row][col - 1] if col > 0 else 0
                top = grid[row - 1][col] if row > 0 else 0
                remove = grid[row - 1][col - 1] if (row > 0 and col > 0) else 0
                grid[row][col] = curr + left + top - remove
                if grid[row][col] <= k:
                    res += 1 
        return res

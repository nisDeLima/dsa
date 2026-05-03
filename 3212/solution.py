class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        dpx = [0] * COLS
        dpy = [0] * COLS
        res = 0
        for row in range(ROWS):
            total_x = 0
            total_y = 0
            for col in range(COLS):
                if grid[row][col] == "X":
                    dpx[col] += 1
                if grid[row][col] == "Y":
                    dpy[col] += 1

                total_x += dpx[col]
                total_y += dpy[col]
                
                if total_x and total_y == total_x:
                    res += 1
        return res

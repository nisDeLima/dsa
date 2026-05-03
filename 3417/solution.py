class Solution:
    def zigzagTraversal_rmv(self, grid: List[List[int]]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0])

        should_add = True
        should_reverse = False
        res = []
        for row in range(ROWS):
            if should_reverse:
                for col in range(COLS - 1, -1, -1):
                    if should_add:
                        res.append(grid[row][col])
                    should_add = not should_add
            else:
                for col in range(COLS):
                    if should_add:
                        res.append(grid[row][col])
                    should_add = not should_add
            should_reverse = not should_reverse
        return res

    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        result = []

        for i in range(m):
            if i % 2 == 0:
                cols = range(n)
            else:
                cols = range(n - 1, -1, -1)

            for j in cols:
                if (i + j) % 2 == 0:
                    result.append(grid[i][j])

        return result 

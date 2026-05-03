class Solution_rmvd:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        res = [[0] * (COLS - k + 1) for _ in range(ROWS - k + 1)]

        def calc_min(row_pos, col_pos):
            row_l, row_r = row_pos
            col_l, col_r = col_pos

            values = []
            for row in range(row_l, row_r + 1):
                for col in range(col_l, col_r + 1):
                    values.append(grid[row][col])

            values.sort()

            if len(values) < 2:
                return 0

            min_diff = float("inf")
            for i in range(1, len(values)):
                if values[i] - values[i - 1] > 0:
                    min_diff = min(min_diff, values[i] - values[i - 1])

            if min_diff == float("inf"):
                min_diff = 0

            return min_diff

        visited = set()

        def rec(row_pos, col_pos):
            if (row_pos, col_pos) in visited:
                return
            visited.add((row_pos, col_pos))

            row_l, row_r = row_pos
            col_l, col_r = col_pos

            if row_r >= ROWS or col_r >= COLS:
                return

            rec((row_l + 1, row_r + 1), (col_l, col_r))
            rec((row_l, row_r), (col_l + 1, col_r + 1))
            res[row_l][col_l] = calc_min(row_pos, col_pos)

        rec((0, k - 1), (0, k - 1))
        return res
class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        res = [[0] * (cols - k + 1) for _ in range(rows - k + 1)]

        def min_pos_diff(window):
            """Min positive difference between adjacent sorted values."""
            best = float('inf')
            for i in range(len(window) - 1):
                d = window[i + 1] - window[i]
                if 0 < d < best:
                    best = d
            return best if best != float('inf') else 0

        for r in range(rows - k + 1):
            # Build initial window for this row
            cur = sorted(grid[r + i][j] for i in range(k) for j in range(k))
            res[r][0] = min_pos_diff(cur)

            # Slide window right
            for c in range(1, cols - k + 1):
                for i in range(k):
                    cur.pop(bisect_left(cur, grid[r + i][c - 1]))
                    insort(cur, grid[r + i][c + k - 1])

                res[r][c] = min_pos_diff(cur)

        return res

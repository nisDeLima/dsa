class Solution_rmvd:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0])
        vals = set()

        def valid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def count(bottom, top, right, left):
            res = 0

            curr = [bottom[0], bottom[1]]
            while curr != list(right):
                res += grid[curr[0]][curr[1]]
                curr[0] -= 1
                curr[1] += 1

            while curr != list(top):
                res += grid[curr[0]][curr[1]]
                curr[0] -= 1
                curr[1] -= 1

            while curr != list(left):
                res += grid[curr[0]][curr[1]]
                curr[0] += 1
                curr[1] -= 1

            while curr != list(bottom):
                res += grid[curr[0]][curr[1]]
                curr[0] += 1
                curr[1] += 1

            return res

        for r in range(ROWS):
            for c in range(COLS):
                vals.add(grid[r][c])

                k = 1
                while True:
                    bottom = (r + k, c)
                    top = (r - k, c)
                    right = (r, c + k)
                    left = (r, c - k)

                    if not all([
                        valid(*bottom),
                        valid(*top),
                        valid(*right),
                        valid(*left)
                    ]):
                        break

                    vals.add(count(bottom, top, right, left))
                    k += 1

        return sorted(vals, reverse=True)[:3]
class Solution_also_rmvd:
    def prefix_pos_diag(self, grid):
        """Prefix sum along \ diagonals (row-1, col-1)"""
        ROWS, COLS = len(grid), len(grid[0])
        # 1-indexed padding: prefix[r][c] = sum along \ from start to grid[r-1][c-1]
        self.prefix_pos = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for row in range(1, ROWS + 1):
            for col in range(1, COLS + 1):
                self.prefix_pos[row][col] = (
                    grid[row - 1][col - 1] + self.prefix_pos[row - 1][col - 1]
                )

    def prefix_neg_diag(self, grid):
        """Prefix sum along / diagonals (row-1, col+1)"""
        ROWS, COLS = len(grid), len(grid[0])
        # 1-indexed rows, but col+1 goes right so we pad col on the RIGHT
        self.prefix_neg = [[0] * (COLS + 2) for _ in range(ROWS + 1)]

        for row in range(1, ROWS + 1):
            for col in range(COLS, 0, -1):
                self.prefix_neg[row][col] = (
                    grid[row - 1][col - 1] + self.prefix_neg[row - 1][col + 1]
                )

    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0])
        vals = set()

        self.prefix_neg_diag(grid)
        self.prefix_pos_diag(grid)

        def valid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def count(bottom, top, right, left):
            bottom, top, right, left = (bottom[0]+1, bottom[1]+1), (top[0]+1, top[1]+1), (right[0]+1, right[1]+1), (left[0]+1, left[1]+1)
            res = 0
            # \ diagonal: top -> right
            res += self.prefix_pos[right[0]][right[1]] - self.prefix_pos[top[0] - 1][top[1] - 1]
            # \ diagonal: left -> bottom
            res += self.prefix_pos[bottom[0]][bottom[1]] - self.prefix_pos[left[0] - 1][left[1] - 1]
            # / diagonal: top -> left
            res += self.prefix_neg[left[0]][left[1]] - self.prefix_neg[top[0] - 1][top[1] + 1]
            # / diagonal: right -> bottom
            res += self.prefix_neg[bottom[0]][bottom[1]] - self.prefix_neg[right[0] - 1][right[1] + 1]

            # corners are counted twice
            res -= grid[top[0] - 1][top[1] - 1]
            res -= grid[bottom[0] - 1][bottom[1] - 1]
            res -= grid[left[0] - 1][left[1] - 1]
            res -= grid[right[0] - 1][right[1] - 1]
            return res 
        for r in range(ROWS):
            for c in range(COLS):
                vals.add(grid[r][c])

                k = 1
                while True:
                    bottom = (r + k, c)
                    top = (r - k, c)
                    right = (r, c + k)
                    left = (r, c - k)

                    if not all([
                        valid(*bottom),
                        valid(*top),
                        valid(*right),
                        valid(*left)
                    ]):
                        break

                    vals.add(count(bottom, top, right, left))
                    k += 1

        return sorted(vals, reverse=True)[:3]
from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0])

        # \ diagonal prefix: dp[r][c] = sum along \ ending at (r-1, c-1)
        pos = [[0] * (COLS + 2) for _ in range(ROWS + 2)]
        # / diagonal prefix: dp[r][c] = sum along / ending at (r-1, c-1)
        neg = [[0] * (COLS + 2) for _ in range(ROWS + 2)]

        for r in range(1, ROWS + 1):
            for c in range(1, COLS + 1):
                pos[r][c] = grid[r - 1][c - 1] + pos[r - 1][c - 1]
                neg[r][c] = grid[r - 1][c - 1] + neg[r - 1][c + 1]

        def pos_sum(r1, c1, r2, c2):
            """Sum along \ from (r1,c1) to (r2,c2), 0-indexed grid coords."""
            return pos[r2 + 1][c2 + 1] - pos[r1][c1]

        def neg_sum(r1, c1, r2, c2):
            """Sum along / from (r1,c1) to (r2,c2), 0-indexed grid coords."""
            return neg[r2 + 1][c2 + 1] - neg[r1][c1 + 2]

        def rhombus(r, c, k):
            top, bottom, left, right = (r - k, c), (r + k, c), (r, c - k), (r, c + k)
            res = 0
            res += pos_sum(*top, *right)       # top -> right  (\)
            res += pos_sum(*left, *bottom)      # left -> bottom (\)
            res += neg_sum(*top, *left)         # top -> left   (/)
            res += neg_sum(*right, *bottom)     # right -> bottom (/)
            # each corner was counted by two segments
            res -= grid[top[0]][top[1]]
            res -= grid[bottom[0]][bottom[1]]
            res -= grid[left[0]][left[1]]
            res -= grid[right[0]][right[1]]
            return res

        vals = set()
        for r in range(ROWS):
            for c in range(COLS):
                vals.add(grid[r][c])
                for k in range(1, min(r, ROWS - 1 - r, c, COLS - 1 - c) + 1):
                    vals.add(rhombus(r, c, k))

        return sorted(vals, reverse=True)[:3]

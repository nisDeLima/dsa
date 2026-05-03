class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        if len(grid) == 1 and len(grid[0]) == 1:
            return True

        moves = {
            1: {"L": (0, 1, "L"), "R": (0, -1, "R")},
            2: {"U": (1, 0, "U"), "D": (-1, 0, "D")},
            3: {"L": (1, 0, "U"), "U": (0, -1, "R")},
            4: {"R": (1, 0, "U"), "D": (0, 1, "L")},
            5: {"U": (0, -1, "R"), "L": (-1, 0, "D")},
            6: {"U": (0, 1, "L"), "L": (-1, 0, "D")},
        }

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, incoming, visited):
            if not (0 <= r < ROWS and 0 <= c < COLS):
                return False

            if (r, c) in visited:
                return False

            move = moves[grid[r][c]].get(incoming)
            if move is None:
                return False

            if (r, c) == (ROWS - 1, COLS - 1):
                return True

            visited.add((r, c))

            dr, dc, nxt = move
            return dfs(r + dr, c + dc, nxt, visited)

        for incoming in ("L", "U", "R", "D"):
            move = moves[grid[0][0]].get(incoming)
            if move is None:
                continue

            dr, dc, _ = move
            if 0 <= dr < ROWS and 0 <= dc < COLS:
                if dfs(0, 0, incoming, set()):
                    return True

        return False

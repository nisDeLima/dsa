class Solution_ttl:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])

        total = 1
        for row in grid:
            for val in row:
                total *= val

        return [[(total // val) % 12345 for val in row] for row in grid]

class Solution_passbutbad:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        flat = []

        for row in range(ROWS):
            for col in range(COLS):
                flat.append(grid[row][col])
        
        prefix = []
        suffix = []

        curr = 1
        for elm in flat:
            prefix.append(curr)
            curr *= elm % 12345

        curr = 1
        for elm in reversed(flat):
            suffix.append(curr)
            curr *= elm % 12345
        
        suffix.reverse()

        idx = 0
        p = [[0] * COLS for _ in range(ROWS)]
        for row in range(ROWS):
            for col in range(COLS):
                p[row][col] = (prefix[idx] * suffix[idx]) % 12345
                idx += 1
        
        return p

class Solution_goodbutcanbebetter:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        flat = [val for row in grid for val in row]
        n = len(flat)

        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * flat[i - 1] % MOD

        suffix = [1] * n
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * flat[i + 1] % MOD

        COLS = len(grid[0])
        return [[(prefix[i] * suffix[i]) % MOD for i, _ in enumerate(row, start=r * COLS)]
                for r, row in enumerate(grid)]
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        flat = [val for row in grid for val in row]
        n = len(flat)
        COLS = len(grid[0])

        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * flat[i - 1] % MOD

        p = [[0] * COLS for _ in range(len(grid))]
        suffix = 1
        for i in range(n - 1, -1, -1):
            p[i // COLS][i % COLS] = prefix[i] * suffix % MOD
            suffix = suffix * flat[i] % MOD

        return p

class Solution:
    def oddCells_del(self, m: int, n: int, indices: List[List[int]]) -> int:
        grid = [([0] * n) for _ in range(m)] 
        res = 0

        for r, c in indices:
            for col in range(n):
                if grid[r][col] % 2 == 0:
                    res += 1
                else:
                    res -= 1
                grid[r][col] += 1
            for row in range(m):
                if grid[row][c] % 2 == 0:
                    res += 1
                else:
                    res -= 1
                grid[row][c] += 1
        
        return res

    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n

        for r, c in indices:
            rows[r] += 1
            cols[c] += 1

        odd_count = 0
        for i in range(m):
            for j in range(n):
                if (rows[i] + cols[j]) % 2 == 1:
                    odd_count += 1

        return odd_count

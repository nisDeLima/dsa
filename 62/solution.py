class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * n

        for row in range(m-1):
            curr = [0] * n
            curr[-1] = 1

            for col in range(n - 2, -1, -1):
                curr[col] = curr[col + 1] + prev[col]
            prev = curr

        return prev[0]

        @cache
        def dfs(row, col):
            if row >= m or col >= n:
                return 0
            if row == m - 1 and col == n - 1:
                return 1

            return dfs(row + 1, col) + dfs(row, col + 1)

        return dfs(0, 0)

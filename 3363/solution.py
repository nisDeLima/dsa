class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        # Child 1: forced diagonal
        c1_sum = 0
        for i in range(n):
            c1_sum += fruits[i][i]
            fruits[i][i] = 0

        NEG_INF = float("-inf")

        # Child 3: starts at (n-1, 0), moves right
        @lru_cache(None)
        def dfs3(i, j, steps):
            if i < 0 or i >= n or j < 0 or j >= n:
                return NEG_INF

            if steps == n - 1:
                return fruits[i][j] if (i, j) == (n - 1, n - 1) else NEG_INF

            return fruits[i][j] + max(
                dfs3(i - 1, j + 1, steps + 1),
                dfs3(i,     j + 1, steps + 1),
                dfs3(i + 1, j + 1, steps + 1),
            )

        # Child 2: starts at (0, n-1), moves down
        @lru_cache(None)
        def dfs2(i, j, steps):
            if i < 0 or i >= n or j < 0 or j >= n:
                return NEG_INF

            if steps == n - 1:
                return fruits[i][j] if (i, j) == (n - 1, n - 1) else NEG_INF

            return fruits[i][j] + max(
                dfs2(i + 1, j - 1, steps + 1),
                dfs2(i + 1, j,     steps + 1),
                dfs2(i + 1, j + 1, steps + 1),
            )

        return c1_sum + dfs2(0, n - 1, 0) + dfs3(n - 1, 0, 0)


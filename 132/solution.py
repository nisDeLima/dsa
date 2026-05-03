from functools import cache
from typing import List


class Solution:
    # =====================================================
    # Solution 1: Full brute-force partition (ground truth)
    # =====================================================

    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def is_palin(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(i, curr):
            if i == n:
                res.append(curr[:])
                return

            for j in range(i, n):
                if is_palin(i, j):
                    curr.append(s[i:j + 1])
                    backtrack(j + 1, curr)
                    curr.pop()

        backtrack(0, [])
        return res

    def minCut_bruteforce(self, s: str) -> int:
        return min(len(p) - 1 for p in self.partition(s))


    # =====================================================
    # Solution 2: Two-pointer DFS (extend vs cut)
    # =====================================================

    def minCut_two_pointer(self, s: str) -> int:
        n = len(s)

        @cache
        def is_palin(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        @cache
        def dfs(l, r):
            if r == n:
                return float("inf")

            cut = float("inf")
            if is_palin(l, r):
                if r == n - 1:
                    return 0
                cut = 1 + dfs(r + 1, r + 1)

            return min(cut, dfs(l, r + 1))

        return dfs(0, 0)


    # =====================================================
    # Solution 3: Clean single-pointer DFS (canonical)
    # =====================================================

    def minCutTopDown(self, s: str) -> int:
        n = len(s)

        @cache
        def is_palin(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        @cache
        def dfs(i):
            if i == n:
                return -1

            res = float("inf")
            for j in range(i, n):
                if is_palin(i, j):
                    res = min(res, 1 + dfs(j + 1))
            return res

        return dfs(0)


    # =====================================================
    # Solution 4: Tabulation (bottom-up version of Solution 3)
    # =====================================================

    def minCut(self, s: str) -> int:
        n = len(s)

        # precompute palindrome table
        is_palin = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or is_palin[i + 1][j - 1]):
                    is_palin[i][j] = True

        # dp[i] = min cuts needed starting at i
        dp = [0] * (n + 1)
        dp[n] = -1  # cancel last cut

        for i in range(n - 1, -1, -1):
            best = float("inf")
            for j in range(i, n):
                if is_palin[i][j]:
                    best = min(best, 1 + dp[j + 1])
            dp[i] = best

        return dp[0]


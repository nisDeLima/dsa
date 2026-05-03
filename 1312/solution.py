class Solution_rmd:
    def minInsertions(self, s: str) -> int:
        @cache
        def rec(l, r):
            if l > r:
                return 0
            
            if s[l] == s[r]:
                return rec(l + 1, r - 1)
            else:
                return min(rec(l + 1, r) + 1, rec(l, r - 1) + 1)
        
        return rec(0, len(s) - 1)
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        # Base case: single characters are already palindromes
        # (dp[i][i] = 0 is already initialized)
        
        # Fill the table: l goes backwards, r goes forwards
        for l in range(n - 1, -1, -1):
            for r in range(l + 1, n):
                if s[l] == s[r]:
                    dp[l][r] = dp[l + 1][r - 1]  # characters match
                else:
                    dp[l][r] = 1 + min(dp[l + 1][r], dp[l][r - 1])
        
        return dp[0][n - 1]

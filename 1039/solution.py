class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def dp(i, j):
            if j - i + 1 < 3: return 0

            res = float("inf")

            for k in range(i + 1, j):
                curr = values[i] * values[k] * values[j]
                res = min(res, curr + dp(i, k) + dp(k, j))
            
            return res
        
        return dp(0, len(values) - 1)

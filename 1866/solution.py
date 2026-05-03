class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        @cache
        def dfs(N, K):
            if N == K:
                return 1 
            if N == 0 or K == 0:
                return 0

            return (dfs(N - 1, K - 1) + (N - 1) * dfs(N - 1, K)) % (10**9 + 7)
        return dfs(n, k)

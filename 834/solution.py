class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        size = [1] * n
        ans = [0] * n

        def dfs1(u: int, p: int, depth: int) -> None:
            ans[0] += depth
            for v in adj[u]:
                if v == p:
                    continue
                dfs1(v, u, depth + 1)
                size[u] += size[v]

        def dfs2(u: int, p: int) -> None:
            for v in adj[u]:
                if v == p:
                    continue
                ans[v] = ans[u] - size[v] + (n - size[v])
                dfs2(v, u)

        dfs1(0, -1, 0)
        dfs2(0, -1)

        return ans


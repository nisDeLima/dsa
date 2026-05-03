class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        adj = [set() for _ in range(n)]

        for r1, r2 in corridors:
            if r2 > r1:
                adj[r1 - 1].add(r2 - 1)
            else:
                adj[r2 - 1].add(r1 - 1)

        res = 0
        for room in range(n):
            for nei in adj[room]:
                res += len(adj[room].intersection(adj[nei]))

        return res

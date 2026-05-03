class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)

        state = [0] * n

        def dfs(node):
            if state[node] != 0:
                return state[node] == 2

            if not adj[node]:
                return node == destination

            state[node] = 1

            for nei in adj[node]:
                if state[nei] == 1:
                    return False
                if not dfs(nei):
                    return False

            state[node] = 2
            return True

        return dfs(source)

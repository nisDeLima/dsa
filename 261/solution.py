class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def dfs(node, par):
            if node in visited:
                return False

            visited.add(node) 

            for nei in adj[node]:
                if nei != par:
                    if not dfs(nei, node):
                        return False

            return True

        return dfs(0, -1) and len(visited) == n

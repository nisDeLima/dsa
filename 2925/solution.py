#class Solution:
#    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
#        adj = [[] for _ in range(len(edges) + 1)]
#        for n1, n2 in edges:
#            adj[n1].append(n2)
#            adj[n2].append(n1)
#        @cache
#        def dfs(node, parent, skipped):
#            # leaf node
#            if len(adj[node]) == 1 and adj[node][0] == parent:
#                return 0 if not skipped else values[node]
#
#            skip = 0
#            take = values[node]
#            for nei in adj[node]:
#                if nei == parent:
#                    continue
#                if skipped:
#                    take += dfs(nei, node, True)
#                else:
#                    skip += dfs(nei, node, True)
#                    take += dfs(nei, node, False)
#            return max(skip, take)
#        return dfs(0, -1, False)
class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        n = len(values)
        g = [[] for _ in range(n)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        total = sum(values)

        def dfs(u, parent):
            if len(g[u]) == 1 and g[u][0] == parent:
                return values[u]
            
            keep = 0
            for v in g[u]:
                if v != parent:
                    keep += dfs(v, u)
            return min(values[u], keep)
        
        leave = dfs(0, -1)
        return total - leave

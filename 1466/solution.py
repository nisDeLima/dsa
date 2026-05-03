class Solution:
    def minReorder_removed(self, n: int, connections: List[List[int]]) -> int:
        # every created route costs 1
        # already existent costs 0
        # prioritize the cheapest ones

        adj = [[] for _ in range(n)] # src: cost, dest

        for src, dest in connections:
            adj[dest].append((0, src))
            adj[src].append((1, dest))

        heap = [(0, 0)] # cost, node
        visited = set()
        removed = 0

        while heap:
            cost, curr = heapq.heappop(heap)
            if curr not in visited:
                visited.add(curr)
                removed += cost

                for nei_cost, nei_node in adj[curr]:
                    if nei_node not in visited:
                        heapq.heappush(heap, (nei_cost, nei_node))
        
        return removed

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(-u)

        def dfs(node, parent):
            changes = 0
            for nei in adj[node]:
                if abs(nei) == parent:
                    continue
                changes += dfs(abs(nei), node) + (nei > 0)
            return changes

        return dfs(0, -1) 

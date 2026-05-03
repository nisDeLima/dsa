class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(set)

        for src, dest in edges:
            adj[src].add(dest)
            adj[dest].add(src)

        leaves = deque()

        for node, edges in adj.items():
            if len(edges) == 1:
                leaves.append(node)

        remaining = n
        while leaves:
            if remaining <= 2:
                return list(leaves)
            remaining -= len(leaves)
            for _ in range(len(leaves)):
                curr = leaves.popleft()
                for nei in adj[curr]:
                    adj[nei].remove(curr)
                    if len(adj[nei]) == 1:
                        leaves.append(nei)

        return [0]

class Solution:
    def collectTheCoins(self, coins, edges):
        n = len(coins)
        if n == 1:
            return 0

        g = [[] for _ in range(n)]
        deg = [0] * n
        
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            deg[u] += 1
            deg[v] += 1

        # Phase 1: prune leaves with NO coins
        q = deque()
        for i in range(n):
            if deg[i] == 1 and coins[i] == 0:
                q.append(i)

        remaining_edges = n - 1  # a tree always has n-1 edges

        while q:
            leaf = q.popleft()
            deg[leaf] -= 1
            for nei in g[leaf]:
                if deg[nei] > 0:
                    deg[nei] -= 1
                    remaining_edges -= 1
                    if deg[nei] == 1 and coins[nei] == 0:
                        q.append(nei)

        # Phase 2: prune TWO layers of leaves with coins
        # because you go in and out to collect
        q = deque()
        for i in range(n):
            if deg[i] == 1:
                q.append(i)

        # two pruning rounds
        for _ in range(2):
            size = len(q)
            for _ in range(size):
                leaf = q.popleft()
                deg[leaf] -= 1
                for nei in g[leaf]:
                    if deg[nei] > 0:
                        deg[nei] -= 1
                        remaining_edges -= 1
                        if deg[nei] == 1:
                            q.append(nei)

        # remaining edges * 2 = total distance
        return max(0, remaining_edges * 2)


# =====================================================
# 1. Optimized Prim's Algorithm (Recommended)
# =====================================================
class PrimOptimized:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        n = len(points)
        visited = [False] * n
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        total = 0

        for _ in range(n):
            u = -1
            for i in range(n):
                if not visited[i] and (u == -1 or min_dist[i] < min_dist[u]):
                    u = i

            visited[u] = True
            total += min_dist[u]

            for v in range(n):
                if not visited[v]:
                    d = manhattan(u, v)
                    if d < min_dist[v]:
                        min_dist[v] = d

        return total


# =====================================================
# 2. Heap-based Prim's Algorithm (Dijkstra-style)
# =====================================================
class PrimHeap:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)
        visited = set()
        heap = [(0, 0)]  # cost, point index
        total_cost = 0

        while len(visited) < n:
            cost, i = heapq.heappop(heap)
            if i in visited:
                continue

            visited.add(i)
            total_cost += cost

            for j in range(n):
                if j not in visited:
                    heapq.heappush(heap, (manhattan(points[i], points[j]), j))

        return total_cost


# =====================================================
# 3. Kruskal's Algorithm (Union-Find)
# =====================================================
class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parents[root_x] = root_y
            self.rank[root_y] += self.rank[root_x]
        else:
            self.parents[root_y] = root_x
            self.rank[root_x] += self.rank[root_y]

        return True


class Kruskal:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)
        edges = []

        # Build all edges (O(n²))
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((manhattan(points[i], points[j]), i, j))

        edges.sort(key=lambda x: x[0])

        uf = UnionFind(n)
        total_cost = 0
        edges_used = 0

        for cost, i, j in edges:
            if uf.merge(i, j):
                total_cost += cost
                edges_used += 1
                if edges_used == n - 1:
                    break

        return total_cost


# =====================================================
# Demo / Testing
# =====================================================
if __name__ == "__main__":
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]

    print("Optimized Prim:", PrimOptimized().minCostConnectPoints(points))
    print("Heap Prim:", PrimHeap().minCostConnectPoints(points))
    print("Kruskal:", Kruskal().minCostConnectPoints(points))


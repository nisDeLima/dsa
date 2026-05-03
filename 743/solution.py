class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n)]

        for src, dest, t in times:
            adj[src - 1].append((t, dest - 1))

        dist = [float('inf')] * n
        start = k - 1
        dist[start] = 0

        pq = [(0, start)]
        heapq.heapify(pq)

        while pq:
            curr_time, node = heapq.heappop(pq)
            if curr_time > dist[node]:
                continue
            for t, nei in adj[node]:
                new_time = curr_time + t
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(pq, (new_time, nei))

        ans = max(dist)
        return ans if ans < float('inf') else -1

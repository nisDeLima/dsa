class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        def cell_cost(r, c):
            entry = (r + 1) * (c + 1)
            if (r == 0 and c == 0) or (r == m - 1 and c == n - 1):
                return entry
            return entry + waitCost[r][c]
        
        heap = [(cell_cost(0, 0), 0, 0)]
        visited = set()
        
        while heap:
            cost, r, c = heapq.heappop(heap)
            
            if (r, c) in visited:
                continue
            visited.add((r, c))
            
            if r == m - 1 and c == n - 1:
                return cost
            
            if c + 1 < n and (r, c + 1) not in visited:
                heapq.heappush(heap, (cost + cell_cost(r, c + 1), r, c + 1))
            
            if r + 1 < m and (r + 1, c) not in visited:
                heapq.heappush(heap, (cost + cell_cost(r + 1, c), r + 1, c))

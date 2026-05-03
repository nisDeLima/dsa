from collections import deque
import heapq
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        queue = deque()

        # Mark thieves and enqueue them with distance 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    queue.append((r, c, 0))
                else:
                    grid[r][c] = -1

        # Multi-source BFS to compute distance to nearest thief
        while queue:
            r, c, dist = queue.popleft()
            next_dist = dist + 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == -1:
                    grid[nr][nc] = next_dist
                    queue.append((nr, nc, next_dist))

        # Maximize minimum safety along the path using a max-heap
        max_heap = [(-grid[0][0], 0, 0)]
        visited = set()
        best = float("inf")

        while max_heap:
            neg_cost, r, c = heapq.heappop(max_heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))

            safety = -neg_cost
            best = min(best, safety)

            if r == rows - 1 and c == cols - 1:
                return best

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    heapq.heappush(max_heap, (-grid[nr][nc], nr, nc))


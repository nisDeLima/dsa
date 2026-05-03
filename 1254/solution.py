class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            # Base case: out of bounds or water
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return False
            if grid[r][c] == 1 or (r, c) in visited:
                return True

            visited.add((r, c))
            res = True  # Assume closed until proven otherwise
            if r in (0, ROWS - 1) or c in (0, COLS - 1):
                res = False

            for dr, dc in DIRECTIONS:
                if not dfs(r + dr, c + dc):
                    res = False
            return res

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0 and (r, c) not in visited:
                    if dfs(r, c):
                        count += 1
        return count
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(r, c):
            q = collections.deque([(r, c)])
            grid[r][c] = 1   # mark visited
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        q.append((nx, ny))

        # 1. Mark all border-connected 0's
        for i in range(rows):
            if grid[i][0] == 0: 
                bfs(i, 0)
            if grid[i][cols-1] == 0: 
                bfs(i, cols-1)

        for j in range(cols):
            if grid[0][j] == 0: 
                bfs(0, j)
            if grid[rows-1][j] == 0: 
                bfs(rows-1, j)

        # 2. Count closed islands in interior
        closed = 0
        for r in range(1, rows-1):
            for c in range(1, cols-1):
                if grid[r][c] == 0:
                    bfs(r, c)
                    closed += 1
        return closed
        
        

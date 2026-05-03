class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        num_islands = 0
        visited_land = set()

        def mark_area(row, col):
            if (
                0 <= row < ROWS and 0<= col < COLS and
                (row, col) not in visited_land and
                grid[row][col] == "1"
            ):
                visited_land.add((row, col))
                for dr, dc in DIRECTIONS:
                    mark_area(row + dr, col + dc)


        for row in range(ROWS):
            for col in range(COLS):
                if (
                    (row, col) not in visited_land and
                    grid[row][col] == "1"
                ):
                    num_islands += 1
                    mark_area(row, col)

        return num_islands

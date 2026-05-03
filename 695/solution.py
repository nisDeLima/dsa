class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        ans = 0

        def get_area(row, col):
            if(
                (row, col) in visited or
                row < 0 or col < 0 or row >= ROWS or col >= COLS or
                grid[row][col] == 0
            ):
                return 0

            visited.add((row, col))
            area = 1
            for d_row, d_col in DIRECTIONS:
                area += get_area(row + d_row, col + d_col)
            return area

        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visited and grid[row][col]:
                    ans = max(ans, get_area(row, col))
        return ans

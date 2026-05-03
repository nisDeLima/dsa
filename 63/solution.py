class Solution:
    def uniquePathsWithObstacles_removed(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS, grid = len(obstacleGrid), len(obstacleGrid[0]), obstacleGrid
        @cache
        def dfs(row, col):
            if (
                row < 0 or row >= ROWS or
                col <0 or col >= COLS or
                grid[row][col] == 1
            ):
                return 0

            elif (row == ROWS - 1 and col == COLS - 1):
                return 1
            
            return dfs(row + 1, col) + dfs(row, col + 1)

        return dfs(0, 0)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS, grid = len(obstacleGrid), len(obstacleGrid[0]), obstacleGrid

        if grid[ROWS - 1][COLS - 1] == 1 or grid[0][0] == 1:
            return 0

        num_ways = 1

        # Setup last col
        for row in range(ROWS - 1, -1, -1):
            if grid[row][COLS - 1] == 1:
                num_ways = 0
            grid[row][COLS - 1] = num_ways

        num_ways = 1
        grid[ROWS - 1][COLS - 1] = 0
        # Setup last row
        for col in range(COLS - 1, -1, -1):
            if grid[ROWS - 1][col] == 1:
                num_ways = 0

            grid[ROWS - 1][col] = num_ways
        

        for row in range(ROWS - 2, - 1, -1):
            for col in range(COLS - 2, -1, -1):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                else:
                    grid[row][col] = grid[row][col + 1] + grid[row + 1][col]
        
        return grid[0][0]



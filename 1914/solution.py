class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        layers = min(rows, cols) // 2

        def layer_positions(layer):
            top = left = layer
            bottom = rows - layer - 1
            right = cols - layer - 1

            for row in range(top, bottom + 1):
                yield row, left

            for col in range(left + 1, right + 1):
                yield bottom, col

            for row in range(bottom - 1, top - 1, -1):
                yield row, right

            for col in range(right - 1, left, -1):
                yield top, col

        result = [row[:] for row in grid]

        for layer in range(layers):
            positions = list(layer_positions(layer))

            values = [
                grid[row][col]
                for row, col in positions
            ]

            size = len(values)

            for idx, (row, col) in enumerate(positions):
                result[row][col] = values[(idx - k) % size]

        return result

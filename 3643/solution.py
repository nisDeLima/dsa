class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        top = x
        bottom = x + k - 1
        col = y + k

        while top < bottom:
            grid[top][y:col], grid[bottom][y:col] = grid[bottom][y:col], grid[top][y:col]
            top += 1
            bottom -= 1
        
        return grid

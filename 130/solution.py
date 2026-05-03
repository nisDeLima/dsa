class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)] 
        ROWS, COLS = len(board), len(board[0])

        def mark_flows(row, col):
            if (
                row < 0 or row >= ROWS or col < 0 or col >= COLS or
                board[row][col] != "O"
            ):
                return
            board[row][col] = "Z"
            for dr, dc in DIRECTIONS:
                mark_flows(row + dr, col + dc)

        for col in range(COLS):
            if board[0][col] == "O":
                mark_flows(0, col)
            if board[ROWS - 1][col] == "O":
                mark_flows(ROWS - 1, col)

        for row in range(ROWS):
            if board[row][0] == "O":
                mark_flows(row, 0)
            if board[row][COLS - 1] == "O":
                mark_flows(row, COLS - 1)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "Z":
                    board[row][col] = "O"



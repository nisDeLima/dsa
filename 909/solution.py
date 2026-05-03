class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        TOTAL = N * N

        label_to_idx = {}
        label = 1
        for row in range(N - 1, -1, -1):
            row_from_bottom = N - 1 - row
            cols = range(N) if row_from_bottom % 2 == 0 else range(N - 1, -1, -1)
            for col in cols:
                label_to_idx[label] = (row, col)
                label += 1

        visited = {1}
        queue = deque([(1, 0)])

        while queue:
            curr, moves = queue.popleft()
            for nxt in range(curr + 1, min(curr + 6, TOTAL) + 1):
                r, c = label_to_idx[nxt]
                if board[r][c] != -1:
                    nxt = board[r][c]
                if nxt == TOTAL:
                    return moves + 1
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, moves + 1))

        return -1

iclass Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        ROWS, COLS = len(grid), len(grid[0])

        bi_prefix = [[[0, 0] for _ in range(COLS)] for _ in range(ROWS)]

        for row in range(ROWS):
            for col in range(COLS):
                top = bi_prefix[row - 1][col] if row > 0 else [0, 0]
                left = bi_prefix[row][col - 1] if col > 0 else [0, 0]
                remove = bi_prefix[row - 1][col - 1] if (col > 0 and row > 0) else [0, 0]

                bi_prefix[row][col][0] = (0 if grid[row][col] else 1) + top[0] + left[0] - remove[0]
                bi_prefix[row][col][1] = (1 if grid[row][col] else 0) + top[1] + left[1] - remove[1]

        def is_leaf(r1, c1, r2, c2):
            for idx in range(2):
                total = bi_prefix[r2][c2][idx]
                if r1 > 0:
                    total -= bi_prefix[r1 - 1][c2][idx]
                if c1 > 0:
                    total -= bi_prefix[r2][c1 - 1][idx]
                if r1 > 0 and c1 > 0:
                    total += bi_prefix[r1 - 1][c1 - 1][idx]
                if total == 0:
                    return True
            return False

        def build_tree(r1, c1, r2, c2):
            if is_leaf(r1, c1, r2, c2):
                return Node(
                    val=bool(grid[r1][c1]),
                    isLeaf=True,
                    topLeft=None, topRight=None,
                    bottomLeft=None, bottomRight=None
                )

            mid_r = r1 + (r2 - r1) // 2
            mid_c = c1 + (c2 - c1) // 2

            curr = Node(val=False, isLeaf=False)
            curr.topLeft     = build_tree(r1,         c1,         mid_r, mid_c)
            curr.topRight    = build_tree(r1,         mid_c + 1,  mid_r, c2)
            curr.bottomLeft  = build_tree(mid_r + 1,  c1,         r2,    mid_c)
            curr.bottomRight = build_tree(mid_r + 1,  mid_c + 1,  r2,    c2)
            return curr

        return build_tree(0, 0, ROWS - 1, COLS - 1)

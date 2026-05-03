class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])

        # Build 2D prefix sum matrix where prefix[r][c] is sum of submatrix (0,0) -> (r-1,c-1)
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(1, rows + 1):
            row_sum = 0
            for c in range(1, cols + 1):
                row_sum += matrix[r - 1][c - 1]
                prefix[r][c] = prefix[r - 1][c] + row_sum

        def area_sum(r1, c1, r2, c2):
            # inclusive rectangle (r1..r2, c1..c2) using 1-based prefix sums
            return (
                prefix[r2][c2]
                - prefix[r1 - 1][c2]
                - prefix[r2][c1 - 1]
                + prefix[r1 - 1][c1 - 1]
            )

        count = 0

        # Fix top and bottom rows, compress into 1D array of column sums
        for top in range(1, rows + 1):
            for bottom in range(top, rows + 1):
                freq = Counter({0: 1})
                running = 0

                for c in range(1, cols + 1):
                    running += area_sum(top, c, bottom, c)
                    count += freq[running - target]
                    freq[running] += 1

        return count

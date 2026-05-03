class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        pos_diag = set()  # row - col
        neg_diag = set()  # row + col
        def backtrack(row):
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if (col in cols or 
                    (row - col) in pos_diag or 
                    (row + col) in neg_diag):
                    continue
                cols.add(col)
                pos_diag.add(row - col)
                neg_diag.add(row + col)
                count += backtrack(row + 1)
                cols.remove(col)
                pos_diag.remove(row - col)
                neg_diag.remove(row + col)
            return count

        return backtrack(0)

class Solution:
    def coloredCells_remove(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return self.coloredCells(n - 1) + (4*(n-1))
        
    def coloredCells(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        res = 1
        for i in range(n):
            res += 4 * (i)
        return res

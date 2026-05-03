class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat = [v for row in grid for v in row]

        r = flat[0] % x
        if any((v % x) != r for v in flat):
            return -1

        flat.sort()
        m = flat[len(flat) // 2]

        return sum(abs(v - m) // x for v in flat)

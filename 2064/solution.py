class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l = 1
        r = max(quantities)

        def valid(num):
            available = n
            for qtd in quantities:
                available -= math.ceil(qtd / num)
                if available < 0:
                    return False
            return True

        while l < r:
            mid = l + (r - l) // 2
            if valid(mid):
                r = mid
            else:
                l = mid + 1
        return r

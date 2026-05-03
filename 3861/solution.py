class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        res = (-1, float("inf"))
        for idx, cap in enumerate(capacity):
            if cap >= itemSize:
                if cap < res[1]:
                    res = (idx, cap)
        return res[0]

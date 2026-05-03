class Solution_rmvd:
    def minPartitions(self, n: str) -> int:
        return int(max(n))
class Solution:
    def minPartitions(self, n: str) -> int:
        for d in "987654321":
            if d in n:
                return int(d)

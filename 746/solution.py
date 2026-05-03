class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def get_min(i):
            if i >= len(cost):
                return 0
            return min(get_min(i + 1), get_min(i + 2)) + cost[i]

        return min(get_min(0), get_min(1))

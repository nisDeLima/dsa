class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        alloys = 0
        def can_build(alloys, machine):
            full_cost = 0
            for metal_type, metal_cnt in enumerate(composition[machine]):
                metal_cnt = max(0, (metal_cnt * alloys) - stock[metal_type])
                full_cost += metal_cnt * cost[metal_type]
                if full_cost > budget:
                    return False
            return True

        for machine in range(k):
            l, r = 0, 1000000000
            while l <= r:
                mid = l + (r - l) // 2
                if can_build(mid, machine):
                    alloys = max(mid, alloys)
                    l = mid + 1
                else:
                    r = mid - 1
        return alloys

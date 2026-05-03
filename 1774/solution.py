class Solution_rmvd:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        
        @cache
        def dfs(curr, toppings):
            if curr >= target:
                return (abs(curr - target), curr)
            
            diff = abs(curr - target)
            cost = curr
            
            for j in range(len(toppings)):
                if toppings[j] > 0:
                    new_toppings = toppings[:j] + (toppings[j] - 1,) + toppings[j+1:]
                    j_diff, j_cost = dfs(curr + toppingCosts[j], new_toppings)
                    if (j_diff < diff) or (j_diff == diff and j_cost < cost):
                        diff = j_diff
                        cost = j_cost
            
            return diff, cost
        
        initial_toppings = tuple([2] * len(toppingCosts))
        
        min_diff = float("inf")
        min_cost = float("inf")
        for b_cost in baseCosts:
            diff, cost = dfs(b_cost, initial_toppings)
            if diff < min_diff or (diff == min_diff and min_cost > cost):
                min_diff = diff
                min_cost = cost
        
        return min_cost

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        best = min(baseCosts)
        
        def dfs(i, curr):
            nonlocal best
            if abs(curr - target) < abs(best - target) or \
               (abs(curr - target) == abs(best - target) and curr < best):
                best = curr
            
            if i == len(toppingCosts) or curr >= target:
                return
            
            for count in range(3):  # 0, 1, or 2 of this topping
                dfs(i + 1, curr + toppingCosts[i] * count)
        
        for base in baseCosts:
            dfs(0, base)
        
        return best

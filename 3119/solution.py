class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        # Early exit
        if budget <= 1:
            return 0

        # Step 1: Split by '.' to get 'x' segments directly
        segments = [len(seg) for seg in road.split('.') if seg]
        if not segments:
            return 0

        # Step 2: Sort largest-first
        segments.sort(reverse=True)

        total = 0
        rem_budget = budget

        # Step 3: Greedy repair
        for seg in segments:
            cost = seg + 1  # 1 extra for activation
            if rem_budget >= cost:
                total += seg
                rem_budget -= cost
            else:
                # partial repair if we have more than 1 left (need activation)
                total += max(0, rem_budget - 1)
                break

        return total

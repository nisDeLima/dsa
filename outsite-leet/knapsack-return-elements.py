"""
0/1 Knapsack Problem
--------------------
Given a list of items, each with a weight and a value, determine the maximum total value
you can carry in a knapsack of limited capacity. You can take each item at most once.

Return both:
- The maximum total value achievable.
- The list of item indices that were taken to achieve that value.

Example:
---------
Input:
    weights = [2, 3, 4, 5]
    values  = [3, 4, 5, 6]
    capacity = 5

Output:
    max_value = 7
    taken_items = [0, 1]  # meaning items 0 and 1 were taken (weights 2+3=5, values 3+4=7)
"""

from typing import List, Tuple
from functools import cache


def knapsack_01(weights: List[int], values: List[int], capacity: int) -> Tuple[int, List[int]]:
    @cache
    def dfs(i, curr_cap):
        if i == len(weights) or curr_cap == 0:
            return 0, ()

        # Item heavier than curr_cap, skip
        diff = curr_cap - weights[i]
        if diff < 0:
            return dfs(i + 1, curr_cap)
        else:
            # take item
            take_count, take_items = dfs(i + 1, diff)
            take_items += (i,)
            take_count += values[i]
            # skip item
            skip_count, skip_items = dfs(i + 1, curr_cap)
            if take_count > skip_count:
                return take_count, take_items
            else:
                return skip_count, skip_items
    return dfs(0, capacity)

# ---------------------------
# Test cases
# ---------------------------
if __name__ == "__main__":
    tests = [
        {
            "weights": [2, 3, 4, 5],
            "values": [3, 4, 5, 6],
            "capacity": 5,
            "expected_value": 7
        },
        {
            "weights": [1, 2, 3],
            "values": [6, 10, 12],
            "capacity": 5,
            "expected_value": 22
        },
        {
            "weights": [4, 2, 3],
            "values": [10, 4, 7],
            "capacity": 5,
            "expected_value": 11
        },
    ]

    for i, t in enumerate(tests, 1):
        result_value, taken = knapsack_01(t["weights"], t["values"], t["capacity"])
        print(f"Test {i}:")
        print(f"  Max Value: {result_value}")
        print(f"  Taken Items: {taken}")
        print(f"  Expected: {t['expected_value']}")
        print("  PASS" if result_value == t["expected_value"] else "  FAIL", "\n")

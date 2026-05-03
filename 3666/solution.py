from math import inf, ceil
import time

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z = s.count('0')  # number of zeros to eliminate

        # Edge case: operation size equals string length
        # Flipping everything at once
        if n == k:
            if z == 0:   return 0   # already all 1s
            elif z == n: return 1   # all 0s, one flip fixes it
            else:        return -1  # mixed, can't fix with full flip

        ans = inf

        # Case 1: use even number of operations
        if z % 2 == 0:
            m = max(ceil(z / k), ceil(z / (n - k)))
            if m % 2 == 1:  # force even
                m += 1
            ans = min(ans, m)

        # Case 2: use odd number of operations
        if z % 2 == k % 2:
            m = max(ceil(z / k), ceil((n - z) / (n - k)))
            if m % 2 == 0:  # force odd
                m += 1
            ans = min(ans, m)

        return ans if ans < inf else -1


if __name__ == "__main__":
    sol = Solution()

    tests = [
        # small — verified expected
        ("110",              1,  1),
        ("0101",             3,  2),
        ("101",              2, -1),
        ("1111",             2,  0),
        ("0000",             2,  2),

        # medium
        ("0" * 10,           3,  None),
        ("01" * 8,           4,  None),
        ("0" * 20,           4,  None),

        # large — watch it not even blink
        ("01" * 1000,        4,  None),
        ("0" * 50000,        7,  None),
        ("01" * 25000,       3,  None),
        ("0" * 100000,       1,  None),  # max constraints
    ]

    for s, k, expected in tests:
        preview = s[:30] + ('...' if len(s) > 30 else '')
        print(f"Running s='{preview}', k={k}, len={len(s)}")
        start = time.time()
        result = sol.minOperations(s, k)
        elapsed = time.time() - start
        status = "✅" if expected is None or result == expected else "❌"
        print(f"{status} result={result}, time={elapsed:.6f}s\n")

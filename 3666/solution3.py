from collections import deque
import time

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z = s.count('0')
        
        if z == 0:
            return 0
        
        visited = {z}
        queue = deque([(z, 0)])
        
        while queue:
            curr_z, moves = queue.popleft()
            curr_o = n - curr_z  # ones = n - zeros
            
            # How many zeros can we flip in one op?
            # min: max(0, k - ones)  -> forced to flip zeros if not enough ones
            # max: min(k, zeros)     -> can't flip more zeros than exist
            min_zero_flips = max(0, k - curr_o)
            max_zero_flips = min(k, curr_z)
            
            for i in range(min_zero_flips, max_zero_flips + 1):
                # flip i zeros and (k-i) ones
                next_z = curr_z - i + (k - i)  # zeros decrease by i, increase by (k-i)
                
                if next_z == 0:
                    return moves + 1
                
                if next_z not in visited and 0 <= next_z <= n:
                    visited.add(next_z)
                    queue.append((next_z, moves + 1))
        
        return -1


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("110",          1,  1),
        ("0101",         3,  2),
        ("101",          2, -1),
        ("1111",         2,  0),
        ("0000",         2,  2),
        ("0" * 10,       3,  None),
        ("01" * 8,       4,  None),
        ("0" * 20,       4,  None),
        ("01" * 1000,    4,  None),
        ("0" * 50000,    7,  None),
        ("0" * 100000,   1,  None),
    ]

    for s, k, expected in tests:
        preview = s[:30] + ('...' if len(s) > 30 else '')
        print(f"Running s='{preview}', k={k}, len={len(s)}")
        start = time.time()
        result = sol.minOperations(s, k)
        elapsed = time.time() - start
        status = "✅" if expected is None or result == expected else "❌"
        print(f"{status} result={result}, time={elapsed:.6f}s\n")

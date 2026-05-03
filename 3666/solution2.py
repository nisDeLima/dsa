from collections import deque

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        
        def goal(state):
            return all(c == '1' for c in state)
        
        def switch(char):
            return '0' if char == '1' else '1'
        
        def get_next(state):
            next_states = []
            
            def backtrack(i, flips_left, curr):
                # Base case: built full state with exactly k flips used
                if i == len(state):
                    if flips_left == 0:
                        next_states.append(tuple(curr))
                    return
                
                # Option 1: don't flip current index
                curr.append(state[i])
                backtrack(i + 1, flips_left, curr)
                curr.pop()
                
                # Option 2: flip current index (only if we still have flips left)
                if flips_left > 0:
                    curr.append(switch(state[i]))
                    backtrack(i + 1, flips_left - 1, curr)
                    curr.pop()
            
            backtrack(0, k, [])
            return next_states
        
        initial = tuple(s)
        
        if goal(initial):
            return 0
        
        visited = {initial}
        queue = deque([(initial, 0)])
        
        while queue:
            curr, moves = queue.popleft()
            
            for next_state in get_next(curr):
                if goal(next_state):
                    return moves + 1
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, moves + 1))
        
        return -1


import time

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("110",      1,  1),
        ("0101",     3,  2),
        ("101",      2, -1),
        ("0" * 10,   3,  None),
        ("01" * 8,   4,  None),
        ("0" * 20,   4,  None),  # this one will hurt
    ]

    for s, k, expected in tests:
        print(f"Running s='{s[:30]}{'...' if len(s) > 30 else ''}', k={k}, len={len(s)}")
        start = time.time()
        result = sol.minOperations(s, k)
        elapsed = time.time() - start
        status = "✅" if expected is None or result == expected else "❌"
        print(f"{status} result={result}, time={elapsed:.3f}s\n")

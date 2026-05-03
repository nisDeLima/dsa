class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        ext = colors
        
        violations = 0
        res = 0
        
        for r in range(len(ext) + k - 1):
            # count violation entering the window
            if r > 0 and ext[r % n] == ext[(r - 1) % n]:
                violations += 1
            
            # shrink: remove the violation at the left edge
            if r >= k:
                if ext[(r - k + 1) % n] == ext[(r - k) % n]:
                    violations -= 1
            
            # window is full size and perfectly alternating
            if r >= k - 1 and violations == 0:
                res += 1
        
        return res

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        max_v = 0
        for a, m in tasks:
            max_v += m
        
        l = 0 
        h = max_v

        tasks.sort(key=lambda x: x[0] - x[1])

        def valid(m):
            curr = m
            for a, m in tasks:
                if curr < m:
                    return False
                curr -= a
            return True

        while l <= h:
            m = l + (h - l) // 2
            if valid(m):
                h = m - 1
            else:
                l = m + 1
        
        return l

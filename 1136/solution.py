class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for prev_course, next_course in relations:
            adj[next_course - 1].append(prev_course - 1)

        can_complete = defaultdict(int)
        checking = set()

        def top_dfs(curr):
            if curr in can_complete:
                return can_complete[curr]
            if curr in checking:
                # cycle detected
                return float("inf")

            checking.add(curr)
            max_nei = 0
            for nei in adj[curr]:
                max_nei = max(top_dfs(nei), max_nei)
            checking.remove(curr)
            can_complete[curr] = max_nei + 1
            return can_complete[curr]

        self.max_size = 0 
        for node in range(n):
            self.max_size = max(self.max_size, top_dfs(node))
        
        return -1 if self.max_size == float("inf") else self.max_size

class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        tree = [[] for _ in range(n)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        def dfs(curr, parent):
            curr_ops = 0
            curr_max_val = 0

            values = []

            for child in tree[curr]:
                if child != parent:
                    max_value, ops = dfs(child, curr)
                    curr_ops += ops
                    values.append(max_value)

                    curr_max_val = max(curr_max_val, max_value)

            for val in values:
                if val < curr_max_val:
                    curr_ops += 1

            return curr_max_val + cost[curr], curr_ops

        _, ops = dfs(0, -1)
        return ops


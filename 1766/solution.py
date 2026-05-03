class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        ans = [-1] * len(nums)
        
        coprimes = defaultdict(list)
        for i in range(1, 51):
            for j in range(1, 51):
                if math.gcd(i, j) == 1:
                    coprimes[i].append(j)
        
        ancestors = defaultdict(list)  # value -> [(node, depth), ...]
        
        def dfs(node, parent, depth):
            # Find closest coprime ancestor
            best_depth = -1
            best_node = -1
            
            # Check all values coprime to current node's value
            for coprime_val in coprimes[nums[node]]:
                if ancestors[coprime_val]:
                    # Get the last one (most recent = deepest = closest)
                    cand_node, cand_depth = ancestors[coprime_val][-1]
                    if cand_depth > best_depth:
                        best_depth = cand_depth
                        best_node = cand_node

            ans[node] = best_node

            # Add current node to ancestors for its VALUE
            ancestors[nums[node]].append((node, depth))

            # Visit children (skip parent to avoid cycles, *burrrp*)
            for child in adj[node]:
                if child != parent:
                    dfs(child, node, depth + 1)

            # BACKTRACK - remove current node when leaving subtree
            ancestors[nums[node]].pop()

        dfs(0, -1, 0)
        return ans

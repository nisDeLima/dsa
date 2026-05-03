class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        # Build bidirectional graph with costs
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append((v, 0))  # Original direction: cost 0
            graph[v].append((u, 1))  # Reversed direction: cost 1
        
        # Step 1: Calculate reversals needed from node 0
        visited = [False] * n
        reversals = [0] * n
        
        def dfs1(node):
            """Calculate reversals needed from node 0"""
            visited[node] = True
            count = 0
            for neighbor, cost in graph[node]:
                if not visited[neighbor]:
                    count += cost + dfs1(neighbor)
            return count
        
        reversals[0] = dfs1(0)
        
        # Step 2: Reroot to calculate for all other nodes
        visited = [False] * n
        
        def dfs2(node, parent_reversals):
            """Propagate reversals to all nodes using rerooting"""
            visited[node] = True
            reversals[node] = parent_reversals
            
            for neighbor, cost in graph[node]:
                if not visited[neighbor]:
                    # When moving root from node to neighbor:
                    # - If cost=0 (edge goes node→neighbor), reversing adds 1
                    # - If cost=1 (edge goes neighbor→node), un-reversing subtracts 1
                    new_reversals = parent_reversals + (1 if cost == 0 else -1)
                    dfs2(neighbor, new_reversals)
        
        dfs2(0, reversals[0])
        
        return reversals

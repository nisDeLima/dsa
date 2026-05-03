class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = defaultdict(list)

        for u, v, c in zip(original, changed, cost):
            adj[u].append((c, v))
        
        @cache
        def calc_dist(src):
            dist = {}
            heap = [(0, src)]
            
            while heap:
                curr_cost, curr = heapq.heappop(heap)
                
                if curr in dist:
                    continue
                    
                dist[curr] = curr_cost
                
                for nei_cost, nei in adj[curr]:
                    if nei not in dist:
                        heapq.heappush(heap, (curr_cost + nei_cost, nei))
            
            return dist
        
        res = 0
        for i in range(len(source)):
            src_c = source[i]
            tgt_c = target[i]
            
            if src_c == tgt_c:
                continue
            
            distances = calc_dist(src_c)
            
            if tgt_c not in distances:
                return -1
            
            res += distances[tgt_c]
        
        return res

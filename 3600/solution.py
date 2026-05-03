class DSet:
    def __init__(self, n):
        self.parents = [node for node in range(n)]
        self.rank = [0] * n
    
    def _get_parent(self, node):
        root = node
        while root != self.parents[root]:
            root = self.parents[root]
        while node != root:
            next_node = self.parents[node]
            self.parents[node] = root
            node = next_node
        return root

    def merge(self, v1, v2):
        parent1, parent2 = self._get_parent(v1), self._get_parent(v2)

        if parent1 == parent2:
            return False
        
        if self.rank[parent1] >= self.rank[parent2]:
            self.parents[parent2] = parent1
            self.rank[parent1] += self.rank[parent2]
        else:
            self.parents[parent1] = parent2
            self.rank[parent2] += self.rank[parent1]
        
        return True
    

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        must_edges = []
        optional_edges = []

        for u, v, s, must in edges:
            if must:
                must_edges.append((s, u, v))
            else:
                optional_edges.append((s, u, v))
        
        must_edges.sort(reverse=True)
        optional_edges.sort(reverse=True)

        ds = DSet(n)
        count = 0
        must_min = float('inf')
        optional_heap = []

        for s, u, v in must_edges:
            if not ds.merge(u, v):
                return -1
            count += 1
            must_min = min(must_min, s)
        
        for s, u, v in optional_edges:
            if ds.merge(u, v):
                count += 1
                optional_heap.append(s)
        
        if count != n - 1:
            return -1

        heapq.heapify(optional_heap)

        upgrades_left = k
        upgraded = []
        while optional_heap and upgrades_left > 0:
            curr = heapq.heappop(optional_heap)
            upgraded.append(curr * 2)
            upgrades_left -= 1
        
        for val in upgraded:
            heapq.heappush(optional_heap, val)
        
        if optional_heap:
            return min(must_min, optional_heap[0])
        else:
            return must_min

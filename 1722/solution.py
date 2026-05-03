class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [0] * n

    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def merge(self, p1, p2):
        parent1, parent2 = self.find(p1), self.find(p2)
        if parent1 == parent2:
            return
        if self.rank[parent1] >= self.rank[parent2]:
            self.parents[parent2] = parent1
            self.rank[parent1] += self.rank[parent2]
        else:
            self.parents[parent1] = parent2
            self.rank[parent2] += self.rank[parent1]


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)

        for u, v in allowedSwaps:
            uf.merge(u, v)

        components = defaultdict(list)
        for i in range(n):
            components[uf.find(i)].append(i)

        result = 0
        for indices in components.values():
            source_vals = Counter(source[i] for i in indices)
            target_vals = Counter(target[i] for i in indices)
            matched = sum((source_vals & target_vals).values())
            result += len(indices) - matched

        return result

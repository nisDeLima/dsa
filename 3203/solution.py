class Solution:
    def minimumDiameterAfterMerge(
        self, edges1: list[list[int]], edges2: list[list[int]]
    ) -> int:
        # Compute diameter of tree 1
        self.diameter = 0
        n = len(edges1) + 1
        adj_list1 = self.build_adj_list(n, edges1)
        self.find_diameter(adj_list1, 0, -1)
        diameter1 = self.diameter  # edge count

        # Compute diameter of tree 2
        self.diameter = 0
        m = len(edges2) + 1
        adj_list2 = self.build_adj_list(m, edges2)
        self.find_diameter(adj_list2, 0, -1)
        diameter2 = self.diameter  # edge count

        # Merge formula using edge-based diameters
        combined = ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1

        return max(diameter1, diameter2, combined)

    def build_adj_list(self, size: int, edges: list[list[int]]) -> list[list[int]]:
        adj_list = [[] for _ in range(size)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        return adj_list

    # DFS returns height in **edges**
    def find_diameter(self, adj_list: list[list[int]], node: int, parent: int) -> int:
        heights = []

        for nei in adj_list[node]:
            if nei == parent:
                continue
            heights.append(self.find_diameter(adj_list, nei, node))

        heights.sort(reverse=True)

        h1 = heights[0] if len(heights) >= 1 else 0
        h2 = heights[1] if len(heights) >= 2 else 0

        # Update diameter using heights (edge count)
        self.diameter = max(self.diameter, h1 + h2)

        # Return height (edges)
        return h1 + 1


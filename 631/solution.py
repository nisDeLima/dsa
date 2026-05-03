from typing import List
from collections import defaultdict, deque

class Excel:
    def __init__(self, height: int, width: str):
        width = (ord(width) - ord("A")) + 1
        self.height = height
        self.width = width
        self.range_grid = [[0] * (width + 1) for _ in range(height + 1)]
        self.grid = [[(0, None)] * width for _ in range(height)]
        self.dependents = defaultdict(set)  # cell -> set of cells that depend on it
        self.dependencies = defaultdict(set)  # cell -> set of cells it depends on

    def compute_range_grid(self):
        for i in range(1, self.height + 1):
            for j in range(1, self.width + 1):
                self.range_grid[i][j] = (
                    self.grid[i-1][j-1][0]
                    + self.range_grid[i-1][j]
                    + self.range_grid[i][j-1]
                    - self.range_grid[i-1][j-1]
                )

    def calculate_range(self, ranges):
        (r1, c1), (r2, c2) = ranges
        r1, c1, r2, c2 = r1+1, c1+1, r2+1, c2+1
        return (
            self.range_grid[r2][c2]
            - self.range_grid[r1-1][c2]
            - self.range_grid[r2][c1-1]
            + self.range_grid[r1-1][c1-1]
        )

    def get_range(self, value):
        if ":" in value:
            ranges = value.split(":")
        else:
            ranges = [value] * 2
        
        formatted_ranges = []
        for rg in ranges:
            col = ord(rg[0]) - ord('A')
            row = int(rg[1:]) - 1
            formatted_ranges.append((row, col))
        
        return formatted_ranges[0], formatted_ranges[1]

    def get_cells_in_range(self, ranges):
        (r1, c1), (r2, c2) = ranges
        cells = []
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                cells.append((r, c))
        return cells

    def update_dependencies(self, cell, numbers):
        # remove old dependencies
        for dep in self.dependencies[cell]:
            self.dependents[dep].discard(cell)
        self.dependencies[cell] = set()

        if numbers is None:
            return

        # add new dependencies
        for num in numbers:
            rng = self.get_range(num)
            for dep_cell in self.get_cells_in_range(rng):
                self.dependencies[cell].add(dep_cell)
                self.dependents[dep_cell].add(cell)

    def topo_recompute(self, start_cells):
        # build in-degree map only for affected subgraph
        in_degree = defaultdict(int)
        visited = set()
        queue = deque(start_cells)

        # BFS to find all affected cells
        affected = set()
        while queue:
            cell = queue.popleft()
            if cell in affected:
                continue
            affected.add(cell)
            for dependent in self.dependents[cell]:
                queue.append(dependent)

        # compute in-degrees within affected subgraph
        for cell in affected:
            in_degree[cell] = sum(1 for dep in self.dependencies[cell] if dep in affected)

        # topo sort — start from cells with no dependencies in affected subgraph
        queue = deque(cell for cell in affected if in_degree[cell] == 0)
        while queue:
            cell = queue.popleft()
            i, j = cell
            _, formula = self.grid[i][j]
            if formula is not None:
                self.compute_range_grid()
                res = 0
                for num in formula:
                    rng = self.get_range(num)
                    res += self.calculate_range(rng)
                self.grid[i][j] = (res, formula)

            for dependent in self.dependents[cell]:
                if dependent in affected:
                    in_degree[dependent] -= 1
                    if in_degree[dependent] == 0:
                        queue.append(dependent)

        self.compute_range_grid()

    def set(self, row: int, column: str, val: int) -> None:
        row, column = row - 1, ord(column) - ord('A')
        self.update_dependencies((row, column), None)
        self.grid[row][column] = (val, None)
        self.compute_range_grid()
        self.topo_recompute([(row, column)])

    def get(self, row: int, column: str) -> int:
        row, column = row - 1, ord(column) - ord('A')
        return self.grid[row][column][0]

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        row, column = row - 1, ord(column) - ord('A')
        self.update_dependencies((row, column), numbers)
        self.compute_range_grid()
        res = 0
        for num in numbers:
            rng = self.get_range(num)
            res += self.calculate_range(rng)
        self.grid[row][column] = (res, numbers)
        self.topo_recompute([(row, column)])
        return self.grid[row][column][0]

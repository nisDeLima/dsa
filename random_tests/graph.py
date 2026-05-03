import heapq
import time
from collections import deque
from dataclasses import dataclass
from typing import List, Tuple, Set, Optional, Callable
import random

@dataclass
class SearchResult:
    """Results from running a search algorithm"""
    path: Optional[List[Tuple[int, int]]]
    nodes_explored: int
    execution_time: float
    path_cost: Optional[float]
    algorithm_name: str

class GridGraph:
    """Represents a 2D grid with movement costs"""

    def __init__(self, size: int, obstacle_probability: float = 0.2, 
                 max_cost: int = 10, seed: Optional[int] = None):
        """
        Generate a random grid graph.

        Args:
            size: Grid dimension (size x size)
            obstacle_probability: Probability of a cell being high-cost obstacle
            max_cost: Maximum cost for obstacle cells (normal cells cost 1)
            seed: Random seed for reproducibility
        """
        if seed is not None:
            random.seed(seed)

        self.size = size
        self.grid = [[1 for _ in range(size)] for _ in range(size)]

        # Add random obstacles (high-cost cells)
        for i in range(size):
            for j in range(size):
                if random.random() < obstacle_probability:
                    self.grid[i][j] = random.randint(2, max_cost)

        # Ensure start and goal are always cost 1
        self.grid[0][0] = 1
        #self.grid[size-1][size-1] = 1

        self.start = (0, 0)
        #self.goal = (size - 1, size - 1)
        self.goal = (size - 1, size - 1)
        self.goal = (random.randint(1, size - 1), random.randint(1, size - 1))
        self.grid[self.goal[0]][self.goal[1]] = 1

    def get_neighbors(self, pos: Tuple[int, int]) -> List[Tuple[Tuple[int, int], float]]:
        """Get valid neighbors and their costs"""
        row, col = pos
        neighbors = []

        # 4-directional movement: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < self.size and 0 <= new_col < self.size:
                cost = self.grid[new_row][new_col]
                neighbors.append(((new_row, new_col), cost))

        return neighbors

    def manhattan_distance(self, pos: Tuple[int, int]) -> float:
        """Manhattan distance heuristic to goal"""
        return abs(pos[0] - self.goal[0]) + abs(pos[1] - self.goal[1])

    def visualize(self) -> str:
        """Simple text visualization of the grid"""
        lines = []
        for i, row in enumerate(self.grid):
            line = ""
            for j, cost in enumerate(row):
                if (i, j) == self.start:
                    line += " S "
                elif (i, j) == self.goal:
                    line += " G "
                else:
                    line += f"{cost:2d} "
            lines.append(line)
        return "\n".join(lines)


def reconstruct_path(came_from: dict, current: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Reconstruct path from came_from dictionary"""
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return list(reversed(path))


def bfs_search(graph: GridGraph) -> SearchResult:
    """Breadth-First Search - explores level by level"""
    start_time = time.time()

    queue = deque([graph.start])
    visited = {graph.start}
    came_from = {}
    nodes_explored = 0

    while queue:
        current = queue.popleft()
        nodes_explored += 1

        if current == graph.goal:
            path = reconstruct_path(came_from, current)
            # BFS doesn't track costs, so calculate path cost
            path_cost = sum(graph.grid[pos[0]][pos[1]] for pos in path[1:])
            return SearchResult(
                path=path,
                nodes_explored=nodes_explored,
                execution_time=time.time() - start_time,
                path_cost=path_cost,
                algorithm_name="BFS"
            )

        for neighbor, _ in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)

    return SearchResult(None, nodes_explored, time.time() - start_time, None, "BFS")


def dfs_search(graph: GridGraph) -> SearchResult:
    """Depth-First Search - explores deep paths first"""
    start_time = time.time()

    stack = [graph.start]
    visited = {graph.start}
    came_from = {}
    nodes_explored = 0

    while stack:
        current = stack.pop()
        nodes_explored += 1

        if current == graph.goal:
            path = reconstruct_path(came_from, current)
            path_cost = sum(graph.grid[pos[0]][pos[1]] for pos in path[1:])
            return SearchResult(
                path=path,
                nodes_explored=nodes_explored,
                execution_time=time.time() - start_time,
                path_cost=path_cost,
                algorithm_name="DFS"
            )

        for neighbor, _ in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                stack.append(neighbor)

    return SearchResult(None, nodes_explored, time.time() - start_time, None, "DFS")


def dijkstra_search(graph: GridGraph) -> SearchResult:
    """Dijkstra's Algorithm - finds optimal path using only g(n)"""
    start_time = time.time()
    # Priority queue: (cost, position)
    pq = [(0, graph.start)]
    g_score = {graph.start: 0}
    came_from = {}
    nodes_explored = 0

    while pq:
        current_cost, current = heapq.heappop(pq)
        nodes_explored += 1

        if current == graph.goal:
            path = reconstruct_path(came_from, current)
            return SearchResult(
                path=path,
                nodes_explored=nodes_explored,
                execution_time=time.time() - start_time,
                path_cost=g_score[current],
                algorithm_name="Dijkstra"
            )
        
        # Skip if we've found a better path already
        if current_cost > g_score.get(current, float('inf')):
            continue
        
        for neighbor, cost in graph.get_neighbors(current):
            tentative_g = g_score[current] + cost
            
            if tentative_g < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = tentative_g
                came_from[neighbor] = current
                heapq.heappush(pq, (tentative_g, neighbor))
    
    return SearchResult(None, nodes_explored, time.time() - start_time, None, "Dijkstra")


def astar_search(graph: GridGraph) -> SearchResult:
    """A* Search - finds optimal path using f(n) = g(n) + h(n)"""
    start_time = time.time()
    
    # Priority queue: (f_score, position)
    pq = [(0, graph.start)]
    g_score = {graph.start: 0}
    came_from = {}
    nodes_explored = 0
    
    while pq:
        current_f, current = heapq.heappop(pq)
        nodes_explored += 1
        
        if current == graph.goal:
            path = reconstruct_path(came_from, current)
            return SearchResult(
                path=path,
                nodes_explored=nodes_explored,
                execution_time=time.time() - start_time,
                path_cost=g_score[current],
                algorithm_name="A*"
            )
        
        # Skip if we've found a better path already
        current_g = g_score.get(current, float('inf'))
        if current_f > current_g + graph.manhattan_distance(current):
            continue
        
        for neighbor, cost in graph.get_neighbors(current):
            tentative_g = g_score[current] + cost
            
            if tentative_g < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = tentative_g
                came_from[neighbor] = current
                f_score = tentative_g + graph.manhattan_distance(neighbor)
                heapq.heappush(pq, (f_score, neighbor))
    
    return SearchResult(None, nodes_explored, time.time() - start_time, None, "A*")


def run_benchmark(num_graphs: int = 10, grid_size: int = 20, 
                  obstacle_prob: float = 0.3, max_cost: int = 10):
    """
    Run benchmark comparing all search algorithms.
    
    Args:
        num_graphs: Number of random graphs to test
        grid_size: Size of each grid (grid_size x grid_size)
        obstacle_prob: Probability of high-cost obstacles
        max_cost: Maximum cost for obstacle cells
    """
    algorithms = [bfs_search, dfs_search, dijkstra_search, astar_search]
    
    print(f"\n{'='*80}")
    print(f"BENCHMARK: {num_graphs} graphs, {grid_size}x{grid_size} grids")
    print(f"Obstacle probability: {obstacle_prob}, Max cost: {max_cost}")
    print(f"{'='*80}\n")
    
    all_results = {algo.__name__: [] for algo in algorithms}
    
    for graph_num in range(num_graphs):
        print(f"Testing graph {graph_num + 1}/{num_graphs}...")
        graph = GridGraph(grid_size, obstacle_prob, max_cost, seed=graph_num)
        print("Running for")
        print("\n" + test_graph.visualize())
        
        for algo in algorithms:
            result = algo(graph)
            all_results[algo.__name__].append(result)
    
    # Print aggregate results
    print(f"\n{'='*80}")
    print("RESULTS")
    print(f"{'='*80}\n")
    
    for algo_name, results in all_results.items():
        valid_results = [r for r in results if r.path is not None]
        
        if not valid_results:
            print(f"{results[0].algorithm_name}: No solutions found")
            continue
        
        avg_nodes = sum(r.nodes_explored for r in valid_results) / len(valid_results)
        avg_time = sum(r.execution_time for r in valid_results) / len(valid_results) * 1000  # ms
        avg_cost = sum(r.path_cost for r in valid_results) / len(valid_results)
        
        print(f"{results[0].algorithm_name}:")
        print(f"  Solved: {len(valid_results)}/{len(results)}")
        print(f"  Avg nodes explored: {avg_nodes:.1f}")
        print(f"  Avg time: {avg_time:.3f} ms")
        print(f"  Avg path cost: {avg_cost:.1f}")
        print()


if __name__ == "__main__":
    print("="*80)
    print("SEARCH ALGORITHM BENCHMARK")
    print("="*80)
    
    # Prompt user for parameters
    print("\nConfigure your benchmark:")
    print("-" * 80)
    
    while True:
        try:
            num_graphs = int(input("Number of test graphs to generate (recommended: 10-50): "))
            if num_graphs < 1:
                print("Come on, you need at least 1 graph. Try again.")
                continue
            if num_graphs > 100:
                print("That's gonna take forever. Maybe dial it back a bit?")
                continue
            break
        except ValueError:
            print("That's not a number, genius. Try again.")
    
    while True:
        try:
            grid_size = int(input("Grid size (NxN, recommended: 10-50): "))
            if grid_size < 5:
                print("Too small. You need at least a 5x5 grid to see meaningful differences.")
                continue
            if grid_size > 100:
                print("That's massive. This will take a while and might explode your RAM. Sure? (y/n): ", end="")
                confirm = input().lower()
                if confirm != 'y':
                    continue
            break
        except ValueError:
            print("Numbers only. Come on.")
    
    while True:
        try:
            obstacle_prob = float(input("Obstacle probability (0.0-0.5 recommended, 0.3 is good): "))
            if not 0 <= obstacle_prob <= 1:
                print("Probability has to be between 0 and 1. Basic statistics.")
                continue
            if obstacle_prob > 0.7:
                print("That's a lot of obstacles. Might not find paths. Continue? (y/n): ", end="")
                confirm = input().lower()
                if confirm != 'y':
                    continue
            break
        except ValueError:
            print("Need a decimal number between 0 and 1.")
    
    while True:
        try:
            max_cost = int(input("Maximum obstacle cost (2-20 recommended): "))
            if max_cost < 2:
                print("Minimum is 2 (normal cells are 1, obstacles need to cost more).")
                continue
            if max_cost > 50:
                print("That's ridiculously expensive. You sure? (y/n): ", end="")
                confirm = input().lower()
                if confirm != 'y':
                    continue
            break
        except ValueError:
            print("Integer values only.")
    
    # Show example grid
    print("\n" + "="*80)
    print("Generating example grid with your parameters...")
    print("="*80)
    test_graph = GridGraph(size=min(grid_size, 15), 
                           obstacle_probability=obstacle_prob, 
                           max_cost=max_cost, 
                           seed=42)
    print("\n" + test_graph.visualize())
    print("\nS = Start (0,0), G = Goal, numbers = movement cost")
    
    print("\n" + "="*80)
    input("Press Enter to start benchmark (this might take a few seconds)...")
    print("="*80)
    
    # Run benchmark
    run_benchmark(
        num_graphs=num_graphs,
        grid_size=grid_size,
        obstacle_prob=obstacle_prob,
        max_cost=max_cost
    )
    
    print("\n" + "="*80)
    print("Benchmark complete! Use these results for your article.")
    print("="*80)

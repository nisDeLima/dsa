## Overview

All three implementations solve the same problem — connecting all points with the minimum total cost, where cost is the **Manhattan distance** between points.
That’s a *Minimum Spanning Tree (MST)* problem.

We’re comparing three ways to build an MST:

1. **Prim’s Algorithm (Optimized, O(n²))**
2. **Prim’s Algorithm with a Heap (O(n² log n))**
3. **Kruskal’s Algorithm with Union-Find (O(n² log n))**

---

### 1. Optimized Prim’s Algorithm

**Concept:**
Start with one node, repeatedly pick the closest unvisited node, and expand the MST.
Instead of a heap, it tracks the cheapest distance to each unvisited node.

**Complexity:**

* **Time:** O(n²)
* **Space:** O(n)

**Advantages:**

* No need to precompute or store edges.
* No heap or extra data structures.
* Most efficient for **dense graphs** (like when every point connects to every other).

**Disadvantages:**

* Code looks slightly old-school (manual min search per iteration).

**When to use:**
→ When `n` ≤ 1000 and the graph is dense — *best choice for LeetCode 1584.*

---

### 2. Heap-based Prim’s Algorithm

**Concept:**
Same idea as Prim’s, but uses a **min-heap** to get the next smallest edge, like Dijkstra’s shortest path.
At each step, push edges from the newly added node.

**Complexity:**

* **Time:** O(n² log n)
* **Space:** O(n²)

**Advantages:**

* Intuitive for people familiar with Dijkstra’s algorithm.
* Easy to visualize the process.

**Disadvantages:**

* Pushes a ton of duplicate edges into the heap.
* Slightly slower due to heap operations and large memory usage.

**When to use:**
→ When you want clearer step-by-step control or debugging visibility.
Not the fastest, but easy to reason about.

---

### 3. Kruskal’s Algorithm with Union-Find

**Concept:**
Sort all edges by weight, then connect them greedily using Union-Find to avoid cycles.

**Complexity:**

* **Time:** O(n² log n) — sorting dominates.
* **Space:** O(n²)

**Advantages:**

* Clean theoretical separation: edge list + DSU.
* Great for understanding MST fundamentals.
* Easy to parallelize or adapt for sparse graphs.

**Disadvantages:**

* Builds and sorts **every edge** (O(n²) edges).
* Eats memory fast when n grows.

**When to use:**
→ When graph is small or sparse, or you specifically want to demonstrate Union-Find logic.

---

### Performance Summary

| Algorithm                | Time Complexity | Space | Pros                   | Cons                 | Best Use Case            |
| ------------------------ | --------------- | ----- | ---------------------- | -------------------- | ------------------------ |
| **Optimized Prim**       | O(n²)           | O(n)  | Fastest, no extra data | Manual scanning      | Dense graphs             |
| **Heap Prim**            | O(n² log n)     | O(n²) | Simple, heap-based     | Slower, memory-heavy | Conceptual clarity       |
| **Kruskal (Union-Find)** | O(n² log n)     | O(n²) | Classic MST structure  | High memory cost     | Small graphs / DSU study |

---

### Verdict

For **LeetCode 1584 (Min Cost to Connect All Points)** or any dense complete graph:

> ✅ **Use the Optimized Prim version.**

It’s the cleanest, fastest, and memory-friendly.
The other two are still worth keeping — one for clarity, the other for theoretical balance.

---

*In short:*

* **PrimOptimized** = the efficient grown-up.
* **PrimHeap** = the readable intern.
* **Kruskal** = the nostalgic professor with Union-Find chalk dust all over him.


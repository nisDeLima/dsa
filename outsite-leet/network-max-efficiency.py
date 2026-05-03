"""
============================================================================
PROBLEM: Maximum Network Efficiency
============================================================================

FULL PROBLEM STATEMENT:

Given a network of n computer systems represented as a rooted tree (with the
master computer 1 as the root), the connections between computers are described
using two arrays, connect_from[] and connect_to[]. Each pair (connect_from[i],
connect_to[i]) represents an undirected edge between two computers. Each computer
has a value assigned to it, represented by the array computer_val[].

To maximize the network's throughput, inefficient systems can be removed. In one
operation, any computer node and all nodes in its subtree, can be removed. The
number of such operations applied is denoted as num_ops.

For a given parameter k, the efficiency of the network after num_ops operations is
calculated as: (sum of values of all remaining computer nodes - k * num_ops).

Determine the maximum possible efficiency after applying some (possibly zero)
operations optimally.

Note: The node values can be negative.

Example:
connect_nodes = 4
connect_from = [1, 2, 3]
connect_to = [2, 3, 4]
computer_val = [3, -7, -8, -9]
k = 5

The network can be represented as:
1:3 --- 2:-7 --- 3:-8 --- 4:-9

It is optimal to remove the subtree rooted at node 2. Then,
efficiency = 3 - (1 * 5) = -2, which is the maximum possible.

Hence, the answer is -2.

Function Description:
Complete the function getMaximumEfficiency with the following parameters:
- int connect_nodes: the number of nodes in the system
- int connect_from[connect_nodes - 1]: one node of the connecting edges
- int connect_to[connect_nodes - 1]: the terminal node of the connecting edges
- int computer_val[connect_nodes]: the values of each computer node
- int k: the parameter for calculating efficiency

Returns:
- int: the maximum possible efficiency after applying some operations optimally

============================================================================
"""


def getMaximumEfficiency(connect_nodes, connect_from, connect_to, computer_val, k):
    """
    TODO: Implement your solution here

    Args:
        connect_nodes (int): Number of nodes in the system
        connect_from (list[int]): Origin nodes of edges (1-indexed)
        connect_to (list[int]): Destination nodes of edges (1-indexed)
        computer_val (list[int]): Values of each computer node (0-indexed)
        k (int): Efficiency parameter

    Returns:
        int: Maximum possible efficiency
    """
    from collections import defaultdict

    adj = defaultdict(list)
    for idx in range(len(connect_from)):
        src = connect_from[idx] - 1
        dst = connect_to[idx] - 1

        adj[src].append(dst)
        adj[dst].append(src)
    #(sum of values of all remaining computer nodes - k * num_ops).
    visited = set()
    def get_max(node):
        visited.add(node)
        take_sum = computer_val[node]
        delete_ops = 0

        for child in adj[node]:
            if child not in visited:
                take_child_sum, take_child_ops = get_max(child)
                take_child_efficiency = take_child_sum - k * take_child_ops
                delete_child_efficiency = -k
                if take_child_efficiency >= delete_child_efficiency:
                    take_sum += take_child_sum
                    delete_ops += take_child_ops
                else:
                    delete_ops += 1

        return take_sum, delete_ops

    total_sum, total_ops = get_max(0)
    return total_sum - k * total_ops

# ============================================================================
# TEST CASES
# ============================================================================

def run_tests():
    print("Running test cases...\n")
    
    # Test Case 1: Example from problem statement
    print("Test Case 1: Basic example")
    connect_nodes = 4
    connect_from = [1, 2, 3]
    connect_to = [2, 3, 4]
    computer_val = [3, -7, -8, -9]
    k = 5
    expected = -2
    result = getMaximumEfficiency(connect_nodes, connect_from, connect_to, computer_val, k)
    print(f"Input: nodes={connect_nodes}, edges={list(zip(connect_from, connect_to))}")
    print(f"Values: {computer_val}, k={k}")
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    print(f"Status: {'✓ PASS' if result == expected else '✗ FAIL'}\n")

    # Test Case 2: All positive values - should keep everything
    print("Test Case 2: All positive values")
    connect_nodes = 3
    connect_from = [1, 1]
    connect_to = [2, 3]
    computer_val = [10, 5, 8]
    k = 100
    expected = 23  # 10 + 5 + 8, no deletions
    result = getMaximumEfficiency(connect_nodes, connect_from, connect_to, computer_val, k)
    print(f"Input: nodes={connect_nodes}, edges={list(zip(connect_from, connect_to))}")
    print(f"Values: {computer_val}, k={k}")
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    print(f"Status: {'✓ PASS' if result == expected else '✗ FAIL'}\n")

    # Test Case 3: All negative values with low k
    print("Test Case 3: All negative values, low deletion cost")
    connect_nodes = 3
    connect_from = [1, 2]
    connect_to = [2, 3]
    computer_val = [-5, -10, -15]
    k = 1
    expected = -6  # Keep only root, delete child subtree
    result = getMaximumEfficiency(connect_nodes, connect_from, connect_to, computer_val, k)
    print(f"Input: nodes={connect_nodes}, edges={list(zip(connect_from, connect_to))}")
    print(f"Values: {computer_val}, k={k}")
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    print(f"Status: {'✓ PASS' if result == expected else '✗ FAIL'}\n")
    
    # Test Case 4: Single node
    print("Test Case 4: Single node")
    connect_nodes = 1
    connect_from = []
    connect_to = []
    computer_val = [42]
    k = 10
    expected = 42  # Just the root, no operations
    result = getMaximumEfficiency(connect_nodes, connect_from, connect_to, computer_val, k)
    print(f"Input: nodes={connect_nodes}, edges={list(zip(connect_from, connect_to))}")
    print(f"Values: {computer_val}, k={k}")
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    print(f"Status: {'✓ PASS' if result == expected else '✗ FAIL'}\n")

    # Test Case 5: Mixed values with strategic deletion
    print("Test Case 5: Mixed values requiring strategic deletion")
    connect_nodes = 5
    connect_from = [1, 1, 2, 2]
    connect_to = [2, 3, 4, 5]
    computer_val = [20, -5, 15, -10, -8]
    k = 3
    expected = 32  # Keep 1, 3; delete subtree at 2 (saves -5, -10, -8 = -23, costs 3)
    result = getMaximumEfficiency(connect_nodes, connect_from, connect_to, computer_val, k)
    print(f"Input: nodes={connect_nodes}, edges={list(zip(connect_from, connect_to))}")
    print(f"Values: {computer_val}, k={k}")
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    print(f"Status: {'✓ PASS' if result == expected else '✗ FAIL'}\n")

    # Test Case 6: High deletion cost discourages deletions
    print("Test Case 6: High deletion cost")
    connect_nodes = 4
    connect_from = [1, 2, 3]
    connect_to = [2, 3, 4]
    computer_val = [5, -2, -3, -1]
    k = 10
    expected = -1  # Better to keep all (-1 total) than delete anything
    result = getMaximumEfficiency(connect_nodes, connect_from, connect_to, computer_val, k)
    print(f"Input: nodes={connect_nodes}, edges={list(zip(connect_from, connect_to))}")
    print(f"Values: {computer_val}, k={k}")
    print(f"Expected: {expected}")
    print(f"Got: {result}")
    print(f"Status: {'✓ PASS' if result == expected else '✗ FAIL'}\n")


if __name__ == "__main__":
    run_tests()

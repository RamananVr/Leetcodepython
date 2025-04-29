import sys
# Increase recursion depth if needed for large inputs
# sys.setrecursionlimit(200000)

"""
LeetCode Question #2925: Maximum Score From Removing Nodes From a Tree
There is an undirected tree with n nodes labeled from 0 to n - 1, and rooted at node 0. You are given a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

You are also given a 0-indexed integer array values of length n, where values[i] is the value associated with the ith node.

You start with a score of 0. In one operation, you can:

Pick any node i.
Add values[i] to your score.
Set values[i] to 0.
A tree is healthy if the sum of values on the path from the root to any leaf node is different than zero.

Return the maximum score you can obtain after performing these operations on the tree any number of times so that it remains healthy.
"""

# Solution using Dynamic Programming on Tree

def solve_problem(input_data):
    """
    Calculates the maximum score obtainable while keeping the tree healthy.

    Args:
        input_data: A tuple containing (n, edges, values).
                    n (int): The number of nodes.
                    edges (list[list[int]]): The edges of the tree.
                    values (list[int]): The values associated with each node.

    Returns:
        int: The maximum score.
    """
    n, edges, values = input_data

    if n == 0:
        return 0
    if n == 1:
        # If n=1, node 0 is root and leaf. Path sum is values[0].
        # To be healthy, final values[0] must be non-zero.
        # If initial values[0] == 0, it cannot be made healthy? Assume valid inputs start healthy or can be made healthy.
        # If initial values[0] != 0, we must keep it. Score = 0.
        # The DFS below handles this correctly.
        pass

    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # memo = {} # Optional: Memoization can be added if needed

    def dfs_min_keep(u, parent):
        """
        Calculates the minimum value sum to keep in the subtree rooted at u
        such that all paths from u to leaves below it have a non-zero sum.
        """
        # if u in memo: return memo[u] # Optional memoization check

        # Check if u is effectively a leaf in this traversal context
        is_leaf_in_subtree = True
        for v in adj[u]:
            if v != parent:
                is_leaf_in_subtree = False
                break

        if is_leaf_in_subtree:
            # Base case: Leaf node. Must keep its value.
            # memo[u] = values[u] # Optional memoization store
            return values[u]

        # Recursive step: Calculate sum of dp[v] for children
        sum_f_children = 0
        for v in adj[u]:
            if v != parent:
                sum_f_children += dfs_min_keep(v, u)

        # dp[u] = min(keep u's value, zero u and keep children paths healthy)
        f_u = min(values[u], sum_f_children)
        # memo[u] = f_u # Optional memoization store
        return f_u

    total_sum = sum(values)

    # Calculate the minimum sum that must be kept starting from the root
    min_sum_to_keep = dfs_min_keep(0, -1)

    # The maximum score is the total sum minus the minimum sum we had to keep
    max_score = total_sum - min_sum_to_keep

    return max_score

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1 (From LeetCode Example 1)
    n1 = 7
    edges1 = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
    values1 = [20,10,9,7,4,3,5]
    input_data_1 = (n1, edges1, values1)
    expected_output_1 = 40
    result1 = solve_problem(input_data_1)
    assert result1 == expected_output_1, f"Test Case 1 Failed: Expected {expected_output_1}, Got {result1}"
    print(f"Test Case 1 Passed: Score = {result1}")

    # Test Case 2 (From LeetCode Example 2)
    n2 = 4
    edges2 = [[0,1],[1,2],[1,3]]
    values2 = [10,10,1,1]
    input_data_2 = (n2, edges2, values2)
    expected_output_2 = 20
    result2 = solve_problem(input_data_2)
    assert result2 == expected_output_2, f"Test Case 2 Failed: Expected {expected_output_2}, Got {result2}"
    print(f"Test Case 2 Passed: Score = {result2}")

    # Test Case 3: Single Node
    n3 = 1
    edges3 = []
    values3 = [10]
    input_data_3 = (n3, edges3, values3)
    expected_output_3 = 0
    result3 = solve_problem(input_data_3)
    assert result3 == expected_output_3, f"Test Case 3 Failed: Expected {expected_output_3}, Got {result3}"
    print(f"Test Case 3 Passed: Score = {result3}")
    
    # Test Case 4: Linear Tree
    n4 = 5
    edges4 = [[0,1],[1,2],[2,3],[3,4]]
    values4 = [10, 2, 3, 4, 5] # Total = 24
    # f(4)=5
    # f(3)=min(4, f(4)=5)=4
    # f(2)=min(3, f(3)=4)=3
    # f(1)=min(2, f(2)=3)=2
    # f(0)=min(10, f(1)=2)=2
    # Score = 24 - 2 = 22
    input_data_4 = (n4, edges4, values4)
    expected_output_4 = 22
    result4 = solve_problem(input_data_4)
    assert result4 == expected_output_4, f"Test Case 4 Failed: Expected {expected_output_4}, Got {result4}"
    print(f"Test Case 4 Passed: Score = {result4}")


    print("\nAll provided test cases passed!")

"""
Time and Space Complexity Analysis

Time Complexity: O(N), where N is the number of nodes. Building the adjacency list takes O(N) time (since there are N-1 edges). The DFS visits each node and edge once, taking O(N + E) = O(N + N-1) = O(N) time. Calculating the total sum also takes O(N).
Space Complexity: O(N). The adjacency list requires O(N + E) = O(N) space. The recursion stack for DFS can go up to O(N) in the worst case (a skewed tree).

Topic: Tree DP (Dynamic Programming on Tree)
"""
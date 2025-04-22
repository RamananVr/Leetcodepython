"""
LeetCode Question #797: All Paths From Source to Target

Problem Statement:
Given a directed, acyclic graph (DAG) of `n` nodes labeled from `0` to `n - 1`, find all possible paths from node `0` to node `n - 1`, and return them in any order.

The graph is given as follows: `graph[i]` is a list of all nodes you can visit from node `i` (i.e., there is a directed edge from node `i` to node `graph[i][j]`).

Constraints:
- `n == graph.length`
- `2 <= n <= 15`
- `0 <= graph[i][j] < n`
- `graph[i][j] != i` (i.e., no self-loops)
- All the elements of `graph[i]` are unique.
- The input graph is guaranteed to be a DAG.

Example:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]

Explanation:
The graph is represented as follows:
0 --> 1 --> 3
 \--> 2 --> 3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
"""

# Solution
def allPathsSourceTarget(graph):
    """
    Finds all paths from node 0 to node n-1 in a directed acyclic graph.

    :param graph: List[List[int]] - adjacency list representation of the graph
    :return: List[List[int]] - all paths from node 0 to node n-1
    """
    def dfs(node, path):
        # If we reach the target node, add the path to the result
        if node == len(graph) - 1:
            result.append(path[:])
            return
        
        # Explore all neighbors of the current node
        for neighbor in graph[node]:
            path.append(neighbor)
            dfs(neighbor, path)
            path.pop()  # Backtrack

    result = []
    dfs(0, [0])  # Start DFS from node 0 with the initial path [0]
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    graph1 = [[1,2],[3],[3],[]]
    print(allPathsSourceTarget(graph1))  # Expected Output: [[0,1,3],[0,2,3]]

    # Test Case 2
    graph2 = [[4,3,1],[3,2,4],[3],[4],[]]
    print(allPathsSourceTarget(graph2))  # Expected Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4]]

    # Test Case 3
    graph3 = [[1],[]]
    print(allPathsSourceTarget(graph3))  # Expected Output: [[0,1]]

    # Test Case 4
    graph4 = [[1,2,3],[4],[4],[4],[]]
    print(allPathsSourceTarget(graph4))  # Expected Output: [[0,1,4],[0,2,4],[0,3,4]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- In the worst case, we explore all possible paths in the graph.
- If there are `n` nodes and each node has up to `m` neighbors, the number of paths can be exponential in `n`.
- Thus, the time complexity is O(2^n).

Space Complexity:
- The space complexity is determined by the recursion stack and the storage of paths in the result list.
- The recursion stack can go up to O(n) in depth, and the result list can store up to O(2^n) paths.
- Thus, the space complexity is O(n + 2^n).
"""

# Topic: Graphs
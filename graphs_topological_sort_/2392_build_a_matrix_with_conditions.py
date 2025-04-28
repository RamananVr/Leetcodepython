"""
LeetCode Question #2392: Build a Matrix With Conditions

Problem Statement:
You are given two integers k and n, and two lists of lists rowConditions and colConditions, where:
- k is the size of the matrix (k x k).
- n is the number of conditions.
- rowConditions[i] = [a, b] means that row a must appear before row b in the matrix.
- colConditions[i] = [c, d] means that column c must appear before column d in the matrix.

Return a k x k matrix that satisfies the given row and column conditions. If there is no valid matrix, return an empty matrix.

The matrix should contain all integers from 1 to k exactly once. The rows and columns of the matrix should be permutations of the integers from 1 to k.

Constraints:
- 2 <= k <= 400
- 0 <= n <= 10^4
- rowConditions and colConditions are lists of pairs [a, b] where 1 <= a, b <= k.

"""

from collections import defaultdict, deque

def buildMatrix(k, rowConditions, colConditions):
    def topological_sort(k, conditions):
        graph = defaultdict(list)
        in_degree = [0] * (k + 1)
        
        # Build the graph and calculate in-degrees
        for u, v in conditions:
            graph[u].append(v)
            in_degree[v] += 1
        
        # Perform topological sort using Kahn's algorithm
        queue = deque([i for i in range(1, k + 1) if in_degree[i] == 0])
        order = []
        
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If the order does not contain all nodes, there is a cycle
        if len(order) != k:
            return []
        
        return order
    
    # Get the row and column orders using topological sort
    row_order = topological_sort(k, rowConditions)
    col_order = topological_sort(k, colConditions)
    
    if not row_order or not col_order:
        return []  # Return an empty matrix if either order is invalid
    
    # Create a mapping from value to index for rows and columns
    row_index = {value: idx for idx, value in enumerate(row_order)}
    col_index = {value: idx for idx, value in enumerate(col_order)}
    
    # Build the matrix
    matrix = [[0] * k for _ in range(k)]
    for value in range(1, k + 1):
        matrix[row_index[value]][col_index[value]] = value
    
    return matrix

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    k = 3
    rowConditions = [[1, 2], [2, 3]]
    colConditions = [[2, 1], [3, 2]]
    print(buildMatrix(k, rowConditions, colConditions))
    # Expected Output: [[0, 0, 1], [3, 0, 0], [0, 2, 0]]

    # Test Case 2
    k = 4
    rowConditions = [[1, 2], [2, 3], [3, 4]]
    colConditions = [[4, 3], [3, 2], [2, 1]]
    print(buildMatrix(k, rowConditions, colConditions))
    # Expected Output: [[0, 0, 0, 1], [0, 0, 2, 0], [0, 3, 0, 0], [4, 0, 0, 0]]

    # Test Case 3
    k = 3
    rowConditions = [[1, 2], [2, 3], [3, 1]]
    colConditions = [[1, 2], [2, 3]]
    print(buildMatrix(k, rowConditions, colConditions))
    # Expected Output: [] (Cycle detected in rowConditions)

"""
Time and Space Complexity Analysis:

1. Topological Sort:
   - Time Complexity: O(k + n), where k is the number of nodes and n is the number of edges (conditions).
   - Space Complexity: O(k + n) for the graph representation and in-degree array.

2. Building the Matrix:
   - Time Complexity: O(k^2) for constructing the matrix.
   - Space Complexity: O(k^2) for the matrix storage.

Overall Complexity:
- Time Complexity: O(k + n + k^2)
- Space Complexity: O(k^2 + k + n)

Topic: Graphs (Topological Sort)
"""
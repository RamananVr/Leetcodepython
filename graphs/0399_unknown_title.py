"""
LeetCode Problem #399: Evaluate Division

Problem Statement:
You are given equations in the format `A / B = k`, where `A` and `B` are variables represented as strings, 
and `k` is a real number (floating-point). Given some queries, return the answers. If the answer does not exist, return -1.0.

The input is always valid. You may assume that evaluating the queries will not result in division by zero 
and that there is no contradiction in the input.

Example:
Input: 
    equations = [["a", "b"], ["b", "c"]], 
    values = [2.0, 3.0], 
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
Output: [6.0, 0.5, -1.0, 1.0, -1.0]

Explanation:
Given: a / b = 2.0, b / c = 3.0
- a / c = (a / b) * (b / c) = 6.0
- b / a = 1 / (a / b) = 0.5
- a / e = -1.0 (no path from a to e)
- a / a = 1.0
- x / x = -1.0 (x is not in the equations)

Constraints:
- 1 <= equations.length <= 20
- equations[i].length == 2
- 1 <= queries.length <= 20
- 1 <= values.length == equations.length <= 20
- 0.0 < values[i] <= 20.0
- All variables represented as strings have a length of 1 to 5.
"""

from collections import defaultdict, deque

def calcEquation(equations, values, queries):
    # Step 1: Build the graph
    graph = defaultdict(dict)
    for (a, b), value in zip(equations, values):
        graph[a][b] = value
        graph[b][a] = 1 / value

    # Step 2: Helper function to perform BFS
    def bfs(start, end):
        if start not in graph or end not in graph:
            return -1.0
        if start == end:
            return 1.0
        
        visited = set()
        queue = deque([(start, 1.0)])  # (current_node, current_product)
        
        while queue:
            current, product = queue.popleft()
            if current == end:
                return product
            visited.add(current)
            
            for neighbor, value in graph[current].items():
                if neighbor not in visited:
                    queue.append((neighbor, product * value))
        
        return -1.0

    # Step 3: Process each query
    results = []
    for start, end in queries:
        results.append(bfs(start, end))
    
    return results

# Example Test Cases
if __name__ == "__main__":
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(calcEquation(equations, values, queries))  # Output: [6.0, 0.5, -1.0, 1.0, -1.0]

    equations = [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]]
    values = [3.0, 4.0, 5.0, 6.0]
    queries = [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"], ["x2", "x9"], ["x9", "x9"]]
    print(calcEquation(equations, values, queries))  # Output: [360.0, 0.008333333333333333, 20.0, 1.0, -1.0, -1.0]

# Time Complexity Analysis:
# Let `n` be the number of equations and `m` be the number of queries.
# - Building the graph takes O(n).
# - Each BFS traversal takes O(V + E), where V is the number of variables and E is the number of edges.
# - In the worst case, we perform BFS for each query, so the total complexity is O(m * (V + E)).

# Space Complexity Analysis:
# - The graph uses O(V + E) space.
# - The BFS queue and visited set use O(V) space in the worst case.
# - Overall space complexity is O(V + E).

# Topic: Graphs